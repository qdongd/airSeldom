from airtest.core.api import touch, device, auto_setup
from airtest.core import api
from airtest.core.error import DeviceConnectionError
from airtest.report.report import LogToHtml
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
import time

from airrun.config import AirTest
from seldom.logging import log
from airrun.config import AirTest
import os

__all__ = ["AirDriver"]


class AirDriver:
    @staticmethod
    def connect_device(script, log_dir):
        try:
            log.info(f"🔗连接设备 -> {AirTest.air_app_info}")
            # connect_device(f"Android://127.0.0.1:5037/{AirTest.air_app_info}")
            auto_setup(script, logdir=log_dir, devices=[f"Android://127.0.0.1:5037/{AirTest.air_app_info}"])
            poco = AndroidUiautomationPoco()
            return poco
        except DeviceConnectionError as error:
            log.error(f"❌设备连接失败 -> {error}")
            raise
        except Exception as error:
            log.error(f"❌设备连接异常 -> {error}")
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

    @staticmethod
    def element(element):
        """poco定位元素"""
        log.info(f"🔍︎find -> {element}")
        elem = AirTest.air_poco(element)
        log.info(f"元素定位结果:{elem.exists()}")
        return elem

    @staticmethod
    def start_app(package):
        """在设备上启动目标应用"""
        log.info(f"启动应用 -> {package}")
        api.start_app(package)

    @staticmethod
    def stop_app(package):
        """终止目标应用在设备上的运行"""
        log.info(f"关闭应用 -> {package}")
        api.stop_app(package)

    @staticmethod
    def clear_app(package):
        """清理设备上的目标应用数据"""
        log.info(f"清理数据 -> {package}")
        api.clear_app(package)

    @staticmethod
    def install_app(filepath):
        """安装应用到设备上"""
        path, filename = os.path.split(filepath)
        log.info(f"安装apk包 -> {filename}")
        api.install(filepath)

    @staticmethod
    def uninstall_app(package):
        """卸载设备上的应用"""
        log.info(f"卸载应用 -> {package}")
        api.uninstall(package)

    @staticmethod
    def touch(v, times=1, **kwargs):
        log.info(f"⭕点击 -> {v}")
        api.touch(v, times=times, **kwargs)

    def assert_equal(self, first, second, msg="", snapshot=True) -> None:
        log.info(f"{first} assert_equal -> {second}.")
        api.assert_equal(first, second, msg=msg, snapshot=snapshot)

    def assert_not_equal(self, first, second, msg="", snapshot=True) -> None:
        log.info(f"{first} assert_not_equal -> {second}.")
        api.assert_not_equal(first, second, msg=msg, snapshot=snapshot)
