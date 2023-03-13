from airtest.core.api import touch, device, auto_setup
from airtest.core import api
from airtest.core.error import DeviceConnectionError
from airtest.report.report import LogToHtml
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

from airrun.config import AirTest
from seldom.logging import log

__all__ = ["AirDriver"]


class AirDriver:
    @staticmethod
    def connect_device(log_dir):
        try:
            log.info(f"🔗连接设备：{AirTest.air_app_info}")
            # connect_device(f"Android://127.0.0.1:5037/{AirTest.air_app_info}")
            auto_setup(__file__, logdir=log_dir, devices=[f"Android://127.0.0.1:5037/{AirTest.air_app_info}"])
            poco = AndroidUiautomationPoco()
            return poco
        except DeviceConnectionError as error:
            log.error(f"❌设备连接失败：{error}")
            raise
        except Exception as error:
            log.error(f"❌设备连接异常：{error}")
            raise

    def mint_wark(self):
        """名特室内机专用点亮"""
        dev = device()
        w, h = dev.get_current_resolution()
        self.touch([w / 2, h / 2])

    @staticmethod
    def airtest_report(log_dir, report_dir):
        h1 = LogToHtml(script_root=__file__, log_root=log_dir,
                       logfile="log.txt", lang='zh',
                       static_root="http://47.112.126.227/airtest-static", plugins=None)
        h1.report(output_file=report_dir)

    def touch(self, v, times=1, **kwargs):
        api.touch(v, times=times, **kwargs)
        log.info(f"⭕点击->{v}")

    def assert_equal(self, first, second, msg="", snapshot=True) -> None:
        log.info(f"{first} assert_equal -> {second}.")
        api.assert_equal(first, second, msg=msg, snapshot=snapshot)

    def assert_not_equal(self, first, second, msg="", snapshot=True) -> None:
        log.info(f"{first} assert_not_equal -> {second}.")
        api.assert_not_equal(first, second, msg=msg, snapshot=snapshot)
