import pytest

from page.page_in import PageIn
from tools.get_driver import GetDriver
import page
from tools.get_log import GetLog
from tools.read_yaml import read_yaml
log = GetLog.get_logger()


class TestTravelLogin:

    # 初始化
    def setup_class(self):
        # 1. 获取driver
        driver = GetDriver.get_web_driver(page.url_mis)
        # 2. 通过统一入口类获取PageTravelLogin对象
        self.mis = PageIn(driver).page_get_PageTravelLogin()

    # 结束
    def teardown_class(self):
        # 调用关闭driver
        GetDriver.quit_web_driver()

    # 测试业务方法
    @pytest.mark.parametrize("username,password,expect", read_yaml("travel_login.yaml"))
    def test_travel_login(self, username, password, expect):
        # 调用登录业务方法
        self.mis.page_travel_login(username, password)
        try:
            # 断言
            assert expect == self.mis.page_get_home()
        except Exception as e:
            log.error("断言出错，错误信息：{}".format(e))
            # 输出错误信息
            print("错误原因： ", e)
            # 截图
            self.mis.base_get_img()

            # 抛异常
            raise
