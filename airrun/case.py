from seldom import case
from airrun.config import AirTest
from airtest.core.api import connect_device
from airtest.report.report import simple_report
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airrun.air_appdriver import AirDriver
from airtest.core import assertions
import time
from setting import REPORTS_DIR, AIRLOG_DIR
import os
from seldom.logging import log


class TestCase(case.TestCase, AirDriver):
    """airTest TestCase class"""

    def start_class(self):
        """
        Hook method for setting up class fixture before running tests in the class.
        """
        pass

    def end_class(self):
        """
        Hook method for deconstructing the class fixture after running all tests in the class.
        """
        pass

    @classmethod
    def setUpClass(cls):
        cls().start_class()

    @classmethod
    def tearDownClass(cls):
        cls().end_class()

    def start(self):
        """
        Hook method for setting up the test fixture before exercising it.
        """
        pass

    def end(self):
        """
        Hook method for deconstructing the test fixture after testing it.
        """
        pass

    def setUp(self):
        # 连接设备
        self.case_time = int(time.time())
        self.log_dir = os.path.join(AIRLOG_DIR, f"{self.case_time}_log")
        if AirTest.air_app_info is not None:
            self.poco = self.connect_device(self.log_dir)
        self.start()
        return self.poco

    def tearDown(self):
        log_dir = self.log_dir
        report_dir = os.path.join(REPORTS_DIR, f"{self.case_time}_report.html")
        self.airtest_report(log_dir=log_dir, report_dir=report_dir)
        self.end()
