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

import polling

from ..utils.chromatogram import AgilentHPLCChromatogram
from ..utils.constants import MAX_CMD_NO
from ..utils.macro import *
from ..utils.method_types import *


class HPLCController:
    """
    Class to control Agilent HPLC systems via Chemstation Macros.
    """

    def __init__(
            self,
            comm_dir: str,
            data_dir: str,
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

    def get_spectrum(self):
        """ Load last chromatogram for any channel in spectra dictionary."""
        last_file = self.data_files[-1] if len(self.data_files) > 0 else None

        if last_file is None:
            raise IndexError

        for channel, spec in self.controller.spectra.items():
            spec.load_spectrum(data_path=last_file, channel=channel)
            self.logger.info("%s chromatogram loaded.", channel)

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
