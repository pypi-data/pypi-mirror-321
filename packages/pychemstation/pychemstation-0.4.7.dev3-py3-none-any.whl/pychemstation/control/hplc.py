"""
Module to provide API for the remote control of the Agilent HPLC systems.

HPLCController sends commands to Chemstation software via a command file.
Answers are received via reply file. On the Chemstation side, a custom
Macro monitors the command file, executes commands and writes to the reply file.
Each command is given a number (cmd_no) to keep track of which commands have
been processed.

Authors: Alexander Hammer, Hessam Mehr, Lucy Hao
"""

import logging
import os
import time
from typing import Union

import polling
from xsdata.formats.dataclass.parsers import XmlParser

from .chromatogram import AgilentHPLCChromatogram, TIME_FORMAT
from ..generated import PumpMethod, DadMethod
from ..utils.constants import MAX_CMD_NO, SEQUENCE_TABLE, METHOD_TIMETABLE
from ..utils.hplc_param_types import HPLCAvailStatus, Command, HPLCErrorStatus, Table, TableOperation, SequenceTable, \
    SequenceEntry, RegisterFlag, MethodTimetable, Param, PType, str_to_status, HPLCRunningStatus, Entry, \
    HPLCMethodParams


class HPLCController:
    """
    Class to control Agilent HPLC systems via Chemstation Macros.
    """

    def __init__(
            self,
            comm_dir: str,
            data_dir: str,
            method_dir: str,
            sequence_dir: str,
            cmd_file: str = "cmd",
            reply_file: str = "reply",
    ):
        """Initialize HPLC controller. The `hplc_talk.mac` macro file must be loaded in the Chemstation software.
        `comm_dir` must match the file path in the macro file.
        
        :param comm_dir: Name of directory for communication, where ChemStation will read and write from. Can be any existing directory.
        :param data_dir: Name of directory that ChemStation saves run data. Must be accessible by ChemStation.
        :param cmd_file: Name of command file
        :param reply_file: Name of reply file
        :raises FileNotFoundError: If either `data_dir`, `method_dir` or `comm_dir` is not a valid directory.
        """
        if os.path.isdir(comm_dir):
            self.cmd_file = os.path.join(comm_dir, cmd_file)
            self.reply_file = os.path.join(comm_dir, reply_file)
            self.cmd_no = 0
        else:
            raise FileNotFoundError(f"comm_dir: {comm_dir} not found.")
        self._most_recent_hplc_status = None

        if os.path.isdir(data_dir):
            self.data_dir = data_dir
        else:
            raise FileNotFoundError(f"data_dir: {data_dir} not found.")

        if os.path.isdir(method_dir):
            self.method_dir = method_dir
        else:
            raise FileNotFoundError(f"method_dir: {method_dir} not found.")

        if os.path.isdir(sequence_dir):
            self.sequence_dir = sequence_dir
        else:
            raise FileNotFoundError(f"method_dir: {method_dir} not found.")

        self.spectra = {
            "A": AgilentHPLCChromatogram(self.data_dir),
            "B": AgilentHPLCChromatogram(self.data_dir),
            "C": AgilentHPLCChromatogram(self.data_dir),
            "D": AgilentHPLCChromatogram(self.data_dir),
        }

        self.data_files: list[str] = []
        self.internal_variables: list[dict[str, str]] = []

        # Create files for Chemstation to communicate with Python
        open(self.cmd_file, "a").close()
        open(self.reply_file, "a").close()

        self.logger = logging.getLogger("hplc_logger")
        self.logger.addHandler(logging.NullHandler())

        self.reset_cmd_counter()

        self.logger.info("HPLC Controller initialized.")

    def _set_status(self):
        """Updates current status of HPLC machine"""
        self._most_recent_hplc_status = self.status()[0]

    def _check_data_status(self) -> bool:
        """Checks if HPLC machine is in an available state, meaning a state that data is not being written.

        :return: whether the HPLC machine is in a safe state to retrieve data back."""
        old_status = self._most_recent_hplc_status
        self._set_status()
        file_exists = os.path.exists(self.data_files[-1]) if len(self.data_files) > 0 else False
        done_writing_data = isinstance(self._most_recent_hplc_status,
                                       HPLCAvailStatus) and old_status != self._most_recent_hplc_status and file_exists
        return done_writing_data

    def check_hplc_ready_with_data(self) -> bool:
        """Checks if ChemStation has finished writing data and can be read back.

        :param method: if you are running a method and want to read back data, the timeout period will be adjusted to be longer than the method's runtime

        :return: Return True if data can be read back, else False.
        """
        self._set_status()

        timeout = 10 * 60
        hplc_run_done = polling.poll(
            lambda: self._check_data_status(),
            timeout=timeout,
            step=30
        )

        return hplc_run_done

    def _send(self, cmd: str, cmd_no: int, num_attempts=5) -> None:
        """Low-level execution primitive. Sends a command string to HPLC.

        :param cmd: string to be sent to HPLC
        :param cmd_no: Command number
        :param num_attempts: Number of attempts to send the command before raising exception.
        :raises IOError: Could not write to command file.
        """
        err = None
        for _ in range(num_attempts):
            time.sleep(1)
            try:
                with open(self.cmd_file, "w", encoding="utf8") as cmd_file:
                    cmd_file.write(f"{cmd_no} {cmd}")
            except IOError as e:
                err = e
                self.logger.warning("Failed to send command; trying again.")
                continue
            else:
                self.logger.info("Sent command #%d: %s.", cmd_no, cmd)
                return
        else:
            raise IOError(f"Failed to send command #{cmd_no}: {cmd}.") from err

    def _receive(self, cmd_no: int, num_attempts=100) -> str:
        """Low-level execution primitive. Recives a response from HPLC.

        :param cmd_no: Command number
        :param num_attempts: Number of retries to open reply file
        :raises IOError: Could not read reply file.
        :return: ChemStation response 
        """
        err = None
        for _ in range(num_attempts):
            time.sleep(1)

            try:
                with open(self.reply_file, "r", encoding="utf_16") as reply_file:
                    response = reply_file.read()
            except OSError as e:
                err = e
                self.logger.warning("Failed to read from reply file; trying again.")
                continue

            try:
                first_line = response.splitlines()[0]
                response_no = int(first_line.split()[0])
            except IndexError as e:
                err = e
                self.logger.warning("Malformed response %s; trying again.", response)
                continue

            # check that response corresponds to sent command
            if response_no == cmd_no:
                self.logger.info("Reply: \n%s", response)
                return response
            else:
                self.logger.warning(
                    "Response #: %d != command #: %d; trying again.",
                    response_no,
                    cmd_no,
                )
                continue
        else:
            raise IOError(f"Failed to receive reply to command #{cmd_no}.") from err

    def sleepy_send(self, cmd: Union[Command, str]):
        self.send("Sleep 0.1")
        self.send(cmd)
        self.send("Sleep 0.1")

    def send(self, cmd: Union[Command, str]):
        """Sends a command to Chemstation.

        :param cmd: Command to be sent to HPLC
        """
        if self.cmd_no == MAX_CMD_NO:
            self.reset_cmd_counter()

        cmd_to_send: str = cmd.value if isinstance(cmd, Command) else cmd
        self.cmd_no += 1
        self._send(cmd_to_send, self.cmd_no)

    def receive(self) -> str:
        """Returns messages received in reply file.

        :return: ChemStation response 
        """
        return self._receive(self.cmd_no)

    def reset_cmd_counter(self):
        """Resets the command counter."""
        self._send(Command.RESET_COUNTER_CMD.value, cmd_no=MAX_CMD_NO + 1)
        self._receive(cmd_no=MAX_CMD_NO + 1)
        self.cmd_no = 0

        self.logger.debug("Reset command counter")

    def sleep(self, seconds: int):
        """Tells the HPLC to wait for a specified number of seconds.

        :param seconds: number of seconds to wait
        """
        self.send(Command.SLEEP_CMD.value.format(seconds=seconds))
        self.logger.debug("Sleep command sent.")

    def standby(self):
        """Switches all modules in standby mode. All lamps and pumps are switched off."""
        self.send(Command.STANDBY_CMD)
        self.logger.debug("Standby command sent.")

    def preprun(self):
        """ Prepares all modules for run. All lamps and pumps are switched on."""
        self.send(Command.PREPRUN_CMD)
        self.logger.debug("PrepRun command sent.")

    def status(self) -> list[Union[HPLCRunningStatus, HPLCAvailStatus, HPLCErrorStatus]]:
        """Get device status(es).

        :return: list of ChemStation's current status
        """
        self.send(Command.GET_STATUS_CMD)
        time.sleep(1)

        try:
            parsed_response = self.receive().splitlines()[1].split()[1:]
        except IOError:
            return [HPLCErrorStatus.NORESPONSE]
        except IndexError:
            return [HPLCErrorStatus.MALFORMED]
        recieved_status = [str_to_status(res) for res in parsed_response]
        self._most_recent_hplc_status = recieved_status[0]
        return recieved_status

    def stop_macro(self):
        """Stops Macro execution. Connection will be lost."""
        self.send(Command.STOP_MACRO_CMD)

    def add_table_row(self, table: Table):
        """Adds a row to the provided table for currently loaded method or sequence.
         Import either the SEQUENCE_TABLE or METHOD_TIMETABLE from hein_analytical_control.constants.
        You can also provide your own table.

        :param table: the table to add a new row to
        """
        self.sleepy_send(TableOperation.NEW_ROW.value.format(register=table.register, table_name=table.name))

    def delete_table(self, table: Table):
        """Deletes the table for the current loaded method or sequence.
         Import either the SEQUENCE_TABLE or METHOD_TIMETABLE from hein_analytical_control.constants.
        You can also provide your own table.

        :param table: the table to delete
        """
        self.send(TableOperation.DELETE_TABLE.value.format(register=table.register, table_name=table.name))

    def new_table(self, table: Table):
        """Creates the table for the currently loaded method or sequence.
         Import either the SEQUENCE_TABLE or METHOD_TIMETABLE from hein_analytical_control.constants.
        You can also provide your own table.

        :param table: the table to create
        """
        self.send(TableOperation.CREATE_TABLE.value.format(register=table.register, table_name=table.name))

    def edit_sequence_table(self, sequence_table: SequenceTable):
        """Updates the currently loaded sequence table with the provided table. This method will delete the existing sequence table and remake it.
        If you would only like to edit a single row of a sequence table, use `edit_sequence_table_row` instead.
        :param sequence_table:
        """
        self.send("Local Rows")
        self.sleep(1)
        self.delete_table(SEQUENCE_TABLE)
        self.sleep(1)
        self.new_table(SEQUENCE_TABLE)
        self.sleep(1)
        self._get_table_rows(SEQUENCE_TABLE)
        for i, row in enumerate(sequence_table.rows):
            self.add_table_row(SEQUENCE_TABLE)
            self.sleep(1)
            self.send(Command.SAVE_SEQUENCE_CMD)
            self.sleep(1)
        self._get_table_rows(SEQUENCE_TABLE)
        self.send(Command.SWITCH_SEQUENCE_CMD)
        for i, row in enumerate(sequence_table.rows):
            self.edit_sequence_table_row(row=row, row_num=i + 1)
            self.sleep(1)
            self.send(Command.SAVE_SEQUENCE_CMD)
            self.sleep(1)

    def edit_sequence_table_row(self, row: SequenceEntry, row_num: int):
        """Edits a row in the sequence table. Assumes the row already exists. If not, call `add_sequence_table_row`.
        :param row: sequence row entry with updated information
        :param row_num: the row to edit, based on 1-based indexing
        """
        if row.name:
            self.sleepy_send(TableOperation.EDIT_ROW_TEXT.value.format(register=SEQUENCE_TABLE.register,
                                                                       table_name=SEQUENCE_TABLE.name,
                                                                       row=row_num,
                                                                       col_name=RegisterFlag.NAME,
                                                                       val=row.name))
        if row.vial_location:
            self.sleepy_send(TableOperation.EDIT_ROW_VAL.value.format(register=SEQUENCE_TABLE.register,
                                                                      table_name=SEQUENCE_TABLE.name,
                                                                      row=row_num,
                                                                      col_name=RegisterFlag.VIAL_LOCATION,
                                                                      val=row.vial_location))
        if row.method:
            self.sleepy_send(TableOperation.EDIT_ROW_TEXT.value.format(register=SEQUENCE_TABLE.register,
                                                                       table_name=SEQUENCE_TABLE.name,
                                                                       row=row_num,
                                                                       col_name=RegisterFlag.NAME,
                                                                       val=row.method))
        if row.inj_vol:
            self.sleepy_send(TableOperation.EDIT_ROW_VAL.value.format(register=SEQUENCE_TABLE.register,
                                                                      table_name=SEQUENCE_TABLE.name,
                                                                      row=row_num,
                                                                      col_name=RegisterFlag.NAME,
                                                                      val=row.inj_vol))

    def edit_method(self, updated_method: MethodTimetable):
        """Updated the currently loaded method in ChemStation with provided values.

        :param updated_method: the method with updated values, to be sent to Chemstation to modify the currently loaded method.
        """
        initial_organic_modifier: Param = updated_method.first_row.organic_modifier
        max_time: Param = updated_method.first_row.maximum_run_time
        temp: Param = updated_method.first_row.temperature
        injvol: Param = updated_method.first_row.inj_vol
        equalib_time: Param = updated_method.first_row.equ_time
        flow: Param = updated_method.first_row.flow

        # Method settings required for all runs
        self.send(TableOperation.DELETE_TABLE.value.format(register=METHOD_TIMETABLE.register,
                                                           table_name=METHOD_TIMETABLE.name, ))
        self._update_method_param(initial_organic_modifier)
        self._update_method_param(flow)
        self._update_method_param(Param(val="Set",
                                        chemstation_key=RegisterFlag.STOPTIME_MODE,
                                        ptype=PType.STR))
        self._update_method_param(max_time)
        self._update_method_param(Param(val="Off",
                                        chemstation_key=RegisterFlag.POSTIME_MODE,
                                        ptype=PType.STR))

        # TODO: set the oven temperature
        # self._hplc_controller.update_method_param("str", "Set", "TemperatureControl_Mode")
        # self._hplc_controller.update_method_param("num", temp, temp.chemstation_key[0])
        # self._hplc_controller.update_method_param("num", temp, temp.chemstation_key[1])
        # self._hplc_controller.update_method_param("str", "Set", "TemperatureControl2_Mode")
        # self._hplc_controller.send("DownloadRCMethod PMP1")

        self.send("DownloadRCMethod PMP1")

        self._update_method_timetable(updated_method.subsequent_rows)

    def _get_table_rows(self, table: Table) -> str:
        self.send(TableOperation.GET_OBJ_HDR_VAL.value.format(internal_val="Row",
                                                              register=table.register,
                                                              table_name=table.name,
                                                              col_name=RegisterFlag.NUM_ROWS, ))
        res = self.receive()
        self.send("Sleep 1")
        self.send('Print Rows')
        return res

    def _update_method_timetable(self, timetable_rows: list[Entry]):
        """Updates the timetable, which is seen when right-clicking the pump GUI in Chemstation to get to the timetable.
        :param updated_method:
        """
        self.send("Local Rows")

        self.delete_table(METHOD_TIMETABLE)
        res = self._get_table_rows(METHOD_TIMETABLE)

        while "ERROR" not in res:
            self.delete_table(METHOD_TIMETABLE)
            res = self._get_table_rows(METHOD_TIMETABLE)
        self.new_table(METHOD_TIMETABLE)
        self._get_table_rows(METHOD_TIMETABLE)

        for i, row in enumerate(timetable_rows):
            self.send("Sleep 1")
            self.send(TableOperation.NEW_ROW.value.format(register=METHOD_TIMETABLE.register,
                                                          table_name=METHOD_TIMETABLE.name))
            self.send("Sleep 1")

            if i == 0:
                self.sleepy_send(TableOperation.NEW_COL_TEXT.value.format(
                    register=METHOD_TIMETABLE.register,
                    table_name=METHOD_TIMETABLE.name,
                    col_name="Function",
                    val=RegisterFlag.SOLVENT_COMPOSITION.value))
                self.sleepy_send(TableOperation.NEW_COL_VAL.value.format(
                    register=METHOD_TIMETABLE.register,
                    table_name=METHOD_TIMETABLE.name,
                    col_name="Time",
                    val=row.start_time))
                self.sleepy_send(TableOperation.NEW_COL_VAL.value.format(
                    register=METHOD_TIMETABLE.register,
                    table_name=METHOD_TIMETABLE.name,
                    col_name=RegisterFlag.SOLVENT_B_COMPOSITION.value,
                    val=row.organic_modifer))
            else:
                self.sleepy_send(TableOperation.EDIT_ROW_TEXT.value.format(
                    register=METHOD_TIMETABLE.register,
                    table_name=METHOD_TIMETABLE.name,
                    row="Rows",
                    col_name="Function",
                    val=RegisterFlag.SOLVENT_COMPOSITION.value))
                self.sleepy_send(TableOperation.EDIT_ROW_VAL.value.format(
                    register=METHOD_TIMETABLE.register,
                    table_name=METHOD_TIMETABLE.name,
                    row="Rows",
                    col_name="Time",
                    val=row.start_time))
                self.sleepy_send(TableOperation.EDIT_ROW_VAL.value.format(
                    register=METHOD_TIMETABLE.register,
                    table_name=METHOD_TIMETABLE.name,
                    row="Rows",
                    col_name=RegisterFlag.SOLVENT_B_COMPOSITION.value,
                    val=row.organic_modifer))

            self.send("Sleep 1")
            self.send("DownloadRCMethod PMP1")
            self.send("Sleep 1")

    def _update_method_param(self, method_param: Param):
        """Change a method parameter, changes what is visibly seen in Chemstation GUI. (changes the first row in the timetable)

        :param method_param: a parameter to update for currently loaded method.
        """
        register = METHOD_TIMETABLE.register
        setting_command = TableOperation.UPDATE_OBJ_HDR_VAL if method_param.ptype == PType.NUM else TableOperation.UPDATE_OBJ_HDR_TEXT
        if isinstance(method_param.chemstation_key, list):
            for register_flag in method_param.chemstation_key:
                self.send(setting_command.value.format(register=register,
                                                       register_flag=register_flag,
                                                       val=method_param.val))
        else:
            self.send(setting_command.value.format(register=register,
                                                   register_flag=method_param.chemstation_key,
                                                   val=method_param.val))
        time.sleep(2)

    def desired_method_already_loaded(self, method_name: str) -> bool:
        """Checks if a given method is already loaded into Chemstation. Method name does not need the ".M" extension.

        :param method_name: a Chemstation method
        :return: True if method is already loaded
        """
        self.send(Command.GET_METHOD_CMD)
        parsed_response = self.receive().splitlines()[1].split()[1:][0]
        return method_name in parsed_response

    def switch_method(self, method_name: str):
        """Allows the user to switch between pre-programmed methods. No need to append '.M'
        to the end of the method name. For example. for the method named 'General-Poroshell.M',
        only 'General-Poroshell' is needed.

        :param method_name: any available method in Chemstation method directory
        :raise IndexError: Response did not have expected format. Try again.
        :raise AssertionError: The desired method is not selected. Try again.
        """
        self.send(
            Command.SWITCH_METHOD_CMD.value.format(method_dir=self.method_dir, method_name=method_name)
        )

        time.sleep(2)
        self.send(Command.GET_METHOD_CMD)
        time.sleep(2)
        # check that method switched
        for _ in range(10):
            try:
                parsed_response = self.receive().splitlines()[1].split()[1:][0]
                break
            except IndexError:
                self.logger.debug("Malformed response. Trying again.")
                continue

        assert parsed_response == f"{method_name}.M", "Switching Methods failed."

    def load_method_details(self, method_name: str) -> MethodTimetable:
        """Retrieve method details of an existing method. Don't need to append ".M" to the end. This assumes the
        organic modifier is in Channel B and that Channel A contains the aq layer. Additionally, assumes
         only two solvents are being used.

        :param method_name: name of method to load details of
        :raises FileNotFoundError: Method does not exist
        :return: method details
        """
        method_folder = f"{method_name}.M"
        method_path = os.path.join(self.method_dir, method_folder, "AgilentPumpDriver1.RapidControl.MethodXML.xml")
        dad_path = os.path.join(self.method_dir, method_folder, "Agilent1200erDadDriver1.RapidControl.MethodXML.xml")

        if os.path.exists(os.path.join(self.method_dir, f"{method_name}.M")):
            parser = XmlParser()
            method = parser.parse(method_path, PumpMethod)
            dad = parser.parse(dad_path, DadMethod)

            organic_modifier = None
            aq_modifier = None

            if len(method.solvent_composition.solvent_element) == 2:
                for solvent in method.solvent_composition.solvent_element:
                    if solvent.channel == "Channel_A":
                        aq_modifier = solvent
                    elif solvent.channel == "Channel_B":
                        organic_modifier = solvent

            return MethodTimetable(
                first_row=HPLCMethodParams(
                    organic_modifier=Param(val=organic_modifier.percentage,
                                           chemstation_key=RegisterFlag.SOLVENT_B_COMPOSITION,
                                           ptype=PType.NUM),
                    flow=Param(val=method.flow,
                               chemstation_key=RegisterFlag.FLOW,
                               ptype=PType.NUM),
                    maximum_run_time=Param(val=method.stop_time,
                                           chemstation_key=RegisterFlag.MAX_TIME,
                                           ptype=PType.NUM),
                    temperature=Param(val=None,
                                      chemstation_key=[RegisterFlag.COLUMN_OVEN_TEMP1,
                                                       RegisterFlag.COLUMN_OVEN_TEMP2],
                                      ptype=PType.NUM),
                    inj_vol=Param(val=None,
                                  chemstation_key=None,
                                  ptype=PType.NUM),
                    equ_time=Param(val=None,
                                   chemstation_key=None,
                                   ptype=PType.NUM)),
                subsequent_rows=[
                    Entry(
                        start_time=tte.time,
                        organic_modifer=tte.percent_b,
                        flow=method.flow
                    ) for tte in method.timetable.timetable_entry
                ],
                dad_wavelengthes=dad.signals.signal,
                organic_modifier=organic_modifier,
                modifier_a=aq_modifier
            )
        else:
            raise FileNotFoundError

    def lamp_on(self):
        """Turns the UV lamp on."""
        self.send(Command.LAMP_ON_CMD)

    def lamp_off(self):
        """Turns the UV lamp off."""
        self.send(Command.LAMP_OFF_CMD)

    def pump_on(self):
        """Turns on the pump on."""
        self.send(Command.PUMP_ON_CMD)

    def pump_off(self):
        """Turns the pump off."""
        self.send(Command.PUMP_OFF_CMD)

    def switch_sequence(self, seq_name: str):
        """Switch to the specified sequence. The sequence name does not need the '.S' extension.
        :param seq_name: The name of the sequence file
        :param sequence_dir: The directory where the sequence file resides
        """
        self.send(f'_SeqFile$ = "{seq_name}.S"')
        self.send(f'_SeqPath$ = "{self.sequence_dir}"')
        self.send(Command.SWITCH_SEQUENCE_CMD)

        time.sleep(2)
        self.send(Command.GET_SEQUENCE_CMD)
        time.sleep(2)
        # check that method switched
        for _ in range(10):
            try:
                parsed_response = self.receive().splitlines()[1].split()[1:][0]
                break
            except IndexError:
                self.logger.debug("Malformed response. Trying again.")
                continue

        assert parsed_response == f"{seq_name}.S", "Switching sequence failed."

    def run_sequence(self, experiment_name: str):
        """Starts the currently loaded sequence, storing data
        under the <data_dir>/<experiment_name>.D folder.
        The <experiment_name> will be appended with a timestamp in the '%Y-%m-%d-%H-%M' format.
        Device must be ready.

        :param experiment_name: Name of the experiment
        """
        timestamp = time.strftime(TIME_FORMAT)

        self.send(
            Command.RUN_SEQUENCE_CMD.value.format(
                data_dir=self.data_dir, experiment_name=experiment_name, timestamp=timestamp
            )
        )

        folder_name = f"{experiment_name}_{timestamp}.D"
        self.data_files.append(os.path.join(self.data_dir, folder_name))
        self.logger.info("Started HPLC run:  %s.", folder_name)

    def start_method(self):
        """Starts and executes currently loaded method to run according to Run Time Checklist. Device must be ready.
         Does not store the folder where data is saved.
         """
        self.send(Command.START_METHOD_CMD)

    def run_method(self, experiment_name: str):
        """This is the preferred method to trigger a run.
        Starts the currently selected method, storing data
        under the <data_dir>/<experiment_name>.D folder.
        The <experiment_name> will be appended with a timestamp in the '%Y-%m-%d-%H-%M' format.
        Device must be ready.

        :param experiment_name: Name of the experiment
        """
        timestamp = time.strftime(TIME_FORMAT)

        self.send(
            Command.RUN_METHOD_CMD.value.format(
                data_dir=self.data_dir, experiment_name=experiment_name, timestamp=timestamp
            )
        )

        folder_name = f"{experiment_name}_{timestamp}.D"
        self.data_files.append(os.path.join(self.data_dir, folder_name))
        self.logger.info("Started HPLC run:  %s.", folder_name)

    def stop_method(self):
        """Stops the run. A dialog window will pop up and manual intervention may be required."""
        self.send(Command.STOP_METHOD_CMD)

    def get_spectrum(self):
        """ Load last chromatogram for any channel in spectra dictionary."""
        last_file = self.data_files[-1] if len(self.data_files) > 0 else None

        if last_file is None:
            raise IndexError

        for channel, spec in self.spectra.items():
            spec.load_spectrum(data_path=last_file, channel=channel)
            self.logger.info("%s chromatogram loaded.", channel)
