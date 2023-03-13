import logging

from airtest.core.api import connect_device

from airrun.config import AirTest
from seldom.running.runner import TestMain

logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)


class Main(TestMain):

    def __init__(self,
                 path: str = None,
                 case: str = None,
                 browser: str = None,
                 base_url: str = None,
                 debug: bool = False,
                 timeout: int = 10,
                 app_server=None,
                 app_info=None,
                 report: str = None,
                 title: str = "Seldom Test Report",
                 tester: str = "Anonymous",
                 description: str = "Test case execution",
                 rerun: int = 0,
                 save_last_run: bool = False,
                 language: str = "en",
                 whitelist: list = [],
                 blacklist: list = [],
                 open: bool = True,
                 auto: bool = True,
                 air_app_info=None
                 ):
        AirTest.air_app_info = air_app_info
        super(Main, self).__init__(path, case, browser, base_url, debug, timeout, app_server, app_info, report, title,
                                   tester, description, rerun, save_last_run, language, whitelist, blacklist, open,
                                   auto)

    def air_connect_device(self, air_app_info):
        # 连接设备
        if AirTest.air_app_info is not None:
            AirTest.driver = connect_device(f"Android://127.0.0.1:5037/{air_app_info}")


main = Main
if __name__ == '__main__':
    main(air_app_info="SCOPACCMUZ", debug=True)
