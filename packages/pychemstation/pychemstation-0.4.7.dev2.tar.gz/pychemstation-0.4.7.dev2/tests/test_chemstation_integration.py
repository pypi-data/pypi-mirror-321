import os
import time
import unittest

from pychemstation.control.comm import HPLCController
from pychemstation.control.method import MethodController
from pychemstation.control.sequence import SequenceController
from pychemstation.utils.macro import *
from pychemstation.utils.method_types import *
from pychemstation.utils.sequence_types import *

# CONSTANTS: paths only work in Hein group HPLC machine in room 242
DEFAULT_COMMAND_PATH = "C:\\Users\\User\\Desktop\\Lucy\\"
DEFAULT_METHOD = "GENERAL-POROSHELL"
DEFAULT_TESTING_METHOD = "GENERAL-POROSHELL-MIN"
DEFAULT_METHOD_DIR = "C:\\ChemStation\\1\\Methods\\"
DATA_DIR = "C:\\Users\\Public\\Documents\\ChemStation\\2\\Data"
SEQUENCE_DIR = "C:\\USERS\\PUBLIC\\DOCUMENTS\\CHEMSTATION\\2\\Sequence"

METHOD_EXAMPLE = "/Users/lucyhao/Codes/heinanalyticalcontrol/tests/methods/General-Poroshell.M"

HEIN_LAB_CONSTANTS = [DEFAULT_COMMAND_PATH, DEFAULT_METHOD_DIR, DATA_DIR, SEQUENCE_DIR]


class TestChemStationIntegration(unittest.TestCase):
    def setUp(self):
        for path in HEIN_LAB_CONSTANTS:
            if not os.path.exists(path):
                self.fail(
                    f"{path} does not exist on your system. If you would like to run tests, please change this path.")

        self.hplc_controller = HPLCController(data_dir=DATA_DIR, comm_dir=DEFAULT_COMMAND_PATH)
        self.method_controller = MethodController(controller=self.hplc_controller, src=DEFAULT_METHOD_DIR)
        self.sequence_controller = SequenceController(controller=self.hplc_controller, src=SEQUENCE_DIR)

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
            self.method_controller.switch(method_name=DEFAULT_METHOD)
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

    def test_run_method(self):
        self.method_controller.run(experiment_name="test_experiment")
        time.sleep(60)
        self.assertTrue(HPLCRunningStatus.has_member_key(self.hplc_controller.status()[0]))
        data_ready = self.method_controller.data_ready()
        self.assertTrue(data_ready)

    def test_load_method_details(self):
        self.method_controller.switch(DEFAULT_METHOD)
        try:
            gp_mtd = self.method_controller.load(DEFAULT_METHOD)
        except Exception as e:
            self.fail(f"Should have not failed, {e}")

    def test_method_update_timetable(self):
        self.method_controller.load(DEFAULT_METHOD)
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
                TimeTableEntry(
                    start_time=0.10,
                    organic_modifer=7,
                    flow=0.34
                ),
                TimeTableEntry(
                    start_time=5,
                    organic_modifer=78,
                    flow=0.55
                )
            ]
        )
        try:
            self.method_controller.edit(new_method)
        except Exception as e:
            self.fail(f"Should have not failed: {e}")

    def test_switch_sequence(self):
        try:
            self.sequence_controller.switch(seq_name="hplcOpt")
        except Exception as e:
            self.fail(f"Should have not expected: {e}")

    def test_edit_sequence_table(self):
        self.sequence_controller.edit_row(SequenceEntry(
            vial_location=1,
        ), 1)

    def test_new_sequence_table(self):
        self.sequence_controller.switch(seq_name="hplcOpt")
        seq_table = SequenceTable(
            name="hplcOpt",
            rows=[
                SequenceEntry(
                    vial_location=10,
                    method="C:\\ChemStation\\1\\Methods\\General-Poroshell",
                    num_inj=3,
                    inj_vol=4,
                    sample_name="Test",
                    sample_type=SampleType.BLANK
                ),
                SequenceEntry(
                    vial_location=3,
                    method="C:\\ChemStation\\1\\Methods\\General-Poroshell",
                    num_inj=3,
                    inj_vol=4,
                    sample_name="Another",
                    sample_type=SampleType.CONTROL,
                ),
            ]
        )
        self.sequence_controller.edit(seq_table)

    def test_run_sequence(self):
        self.sequence_controller.switch(seq_name="hplcOpt")
        seq_table = SequenceTable(
            name="hplcOpt",
            rows=[
                SequenceEntry(
                    vial_location=1,
                    method="C:\\ChemStation\\1\\Methods\\General-Poroshell",
                    num_inj=1,
                    inj_vol=1,
                    sample_name="Test",
                    sample_type=SampleType.SAMPLE
                ),
            ]
        )
        self.sequence_controller.edit(seq_table)
        self.sequence_controller.run(seq_table)
        data_ready = self.sequence_controller.data_ready()
        self.assertTrue(data_ready)


if __name__ == '__main__':
    unittest.main()
