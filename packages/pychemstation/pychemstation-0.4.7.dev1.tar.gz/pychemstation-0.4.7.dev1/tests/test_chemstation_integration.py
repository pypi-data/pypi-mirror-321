import os
import time
import unittest

from pychemstation.control.hplc import HPLCController
from pychemstation.utils.hplc_param_types import SequenceEntry, Entry, PType, Param, RegisterFlag, HPLCMethodParams, \
    MethodTimetable, HPLCRunningStatus, Command, HPLCAvailStatus, SequenceTable

# CONSTANTS: paths only work in Hein group HPLC machine in room 242
DEFAULT_COMMAND_PATH = "C:\\Users\\User\\Desktop\\Lucy\\"
DEFAULT_METHOD = "GENERAL-POROSHELL"
DEFAULT_TESTING_METHOD = "GENERAL-POROSHELL-MIN"
DEFAULT_METHOD_DIR = "C:\\ChemStation\\1\\Methods\\"
DATA_DIR = "C:\\Users\\Public\\Documents\\ChemStation\\2\\Data"
SEQUENCE_DIR = "C:\\USERS\\PUBLIC\\DOCUMENTS\\CHEMSTATION\\2\\Sequence"

METHOD_EXAMPLE = "/Users/lucyhao/Codes/heinanalyticalcontrol/tests/methods/General-Poroshell.M"

HEIN_LAB_CONSTANTS = [DEFAULT_COMMAND_PATH, DEFAULT_METHOD_DIR, DATA_DIR, SEQUENCE_DIR]


class TestChemstationPaths(unittest.TestCase):
    def test_init_right_comm_path(self):
        try:
            HPLCController(data_dir=DATA_DIR, comm_dir=DEFAULT_COMMAND_PATH, method_dir=DEFAULT_METHOD_DIR,
                           sequence_dir=SEQUENCE_DIR)
        except FileNotFoundError:
            self.fail("Should not throw error")

    def test_init_wrong_data_dir(self):
        try:
            HPLCController(data_dir=DATA_DIR + "\\fake", comm_dir=DEFAULT_COMMAND_PATH, method_dir=DEFAULT_METHOD_DIR,
                           sequence_dir=SEQUENCE_DIR)
            self.fail("FileNotFoundError should be thrown.")
        except FileNotFoundError:
            pass

    def test_init_wrong_comm_dir(self):
        try:
            HPLCController(data_dir=DATA_DIR, comm_dir=DEFAULT_COMMAND_PATH + "\\fake", method_dir=DEFAULT_METHOD_DIR,
                           sequence_dir=SEQUENCE_DIR)
            self.fail("FileNotFoundError should be thrown.")
        except FileNotFoundError:
            pass

    def test_init_wrong_method_dir(self):
        try:
            HPLCController(data_dir=DATA_DIR, comm_dir=DEFAULT_COMMAND_PATH, method_dir=DEFAULT_METHOD_DIR + "fake",
                           sequence_dir=SEQUENCE_DIR)
            self.fail("FileNotFoundError should be thrown.")
        except FileNotFoundError:
            pass


class TestChemStationIntegration(unittest.TestCase):
    def setUp(self):
        for path in HEIN_LAB_CONSTANTS:
            if not os.path.exists(path):
                self.fail(
                    f"{path} does not exist on your system. If you would like to run tests, please change this path.")

        self.hplc_controller = HPLCController(data_dir=DATA_DIR,
                                              comm_dir=DEFAULT_COMMAND_PATH,
                                              method_dir=DEFAULT_METHOD_DIR,
                                              sequence_dir=SEQUENCE_DIR)

    def test_status_check_standby(self):
        self.hplc_controller.standby()
        self.assertTrue(self.hplc_controller.status()[0] in [HPLCAvailStatus.STANDBY, HPLCRunningStatus.NOTREADY])

    def test_status_check_preprun(self):
        self.hplc_controller.preprun()
        self.assertEqual(HPLCAvailStatus.PRERUN, self.hplc_controller.status()[0])

    def test_send_command(self):
        try:
            self.hplc_controller.send(Command.GET_METHOD_CMD)
        except Exception as e:
            self.fail(f"Should not throw error: {e}")

    def test_send_str(self):
        try:
            self.hplc_controller.send("Local TestNum")
            self.hplc_controller.send("TestNum = 0")
        except Exception as e:
            self.fail(f"Should not throw error: {e}")

    def test_get_response(self):
        try:
            self.hplc_controller.switch_method(method_name=DEFAULT_METHOD)
            self.hplc_controller.send(Command.GET_METHOD_CMD)
            res = self.hplc_controller.receive()
            self.assertTrue(DEFAULT_METHOD in res)
        except Exception as e:
            self.fail(f"Should not throw error: {e}")

    def test_pump_lamp(self):
        pump_lamp = [
            ("response", self.hplc_controller.lamp_on),
            ("response", self.hplc_controller.lamp_off),
            ("response", self.hplc_controller.pump_on),
            ("response", self.hplc_controller.pump_off),
        ]

        for operation in pump_lamp:
            try:
                operation[1]()
            except Exception as e:
                self.fail(f"Failed due to: {e}")

    def test_start_method(self):
        self.hplc_controller.start_method()
        time.sleep(60)
        self.assertTrue(HPLCRunningStatus.has_member_key(self.hplc_controller.status()[0]))

    def test_run_method(self):
        self.hplc_controller.run_method(experiment_name="test_experiment")
        time.sleep(60)
        self.assertTrue(HPLCRunningStatus.has_member_key(self.hplc_controller.status()[0]))
        data_ready = self.hplc_controller.check_hplc_ready_with_data()
        self.assertTrue(data_ready)

    def test_load_method_details(self):
        self.hplc_controller.switch_method(DEFAULT_METHOD)
        try:
            gp_mtd = self.hplc_controller.load_method_details(DEFAULT_METHOD)
        except Exception as e:
            self.fail(f"Should have not failed, {e}")

    def test_method_update_timetable(self):
        new_method = MethodTimetable(
            first_row=HPLCMethodParams(
                organic_modifier=Param(val=7,
                                       chemstation_key=RegisterFlag.SOLVENT_B_COMPOSITION,
                                       ptype=PType.NUM),
                flow=Param(val=0.44,
                           chemstation_key=RegisterFlag.FLOW,
                           ptype=PType.NUM),
                maximum_run_time=Param(val=10,
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
                    start_time=0.10,
                    organic_modifer=7,
                    flow=0.34
                ),
                Entry(
                    start_time=5,
                    organic_modifer=78,
                    flow=0.55
                )
            ]
        )
        try:
            self.hplc_controller.edit_method(new_method)
        except Exception as e:
            self.fail(f"Should have not failed: {e}")

    def test_switch_sequence(self):
        try:
            self.hplc_controller.switch_sequence(seq_name="hplcOpt")
        except Exception as e:
            self.fail(f"Should have not expected: {e}")

    def test_edit_sequence_table(self):
        self.hplc_controller.edit_sequence_table_row(SequenceEntry(
            vial_location=1,
        ), 1)

    def test_new_sequence_table(self):
        self.hplc_controller.switch_sequence(seq_name="hplcOpt")
        seq_table = SequenceTable(
            rows=[
                SequenceEntry(
                    vial_location=10,
                ),
                SequenceEntry(
                    vial_location=2,
                ),
                SequenceEntry(
                    vial_location=8,
                ),
                SequenceEntry(
                    vial_location=9,
                )
            ]
        )
        self.hplc_controller.edit_sequence_table(seq_table)


if __name__ == '__main__':
    unittest.main()
