from time import sleep

from base.base import Base
import page
from tools.get_log import GetLog

log = GetLog.get_logger()


class PageTravelLogin(Base):
    # 输入用户名
    def page_input_username(self, username):
        # 调用父类中输入方法
        self.base_input(page.travel_username, username)

    # 输入密码
    def page_input_password(self, password):
        # 调用父类中输入方法
        self.base_input(page.travel_password, password)

    # 点击登录按钮
    def page_click_login_btn(self):
        # 调用父类中点击方法
        sleep(1)
        self.base_click(page.travel_login_btn)

    # 获取系统主页封装 -> 测试脚本层断言使用
    def page_get_home(self):
        # 调用父类中 获取文本方法
        return self.base_get_text(page.travel_home)

    # 组合业务方法 -> 测试脚本层调用
    def page_travel_login(self, username, password):
        log.info("正在调用后台管理系统登录业务方法，用户名：{} 密码：{}".format(username, password))
        """提示：调用相同页面操作步骤，跨页面暂时不考虑"""
        self.page_input_username(username)
        self.page_input_password(password)
        self.page_click_login_btn()

    # 组合业务方法 -> 增加酒店依赖调用
    def page_travel_login_success(self, username="admin", password="123456"):
        log.info("正在调用后台管理系统登录业务方法，用户名：{} 密码：{}".format(username, password))
        """提示：调用相同页面操作步骤，跨页面暂时不考虑"""
        self.page_input_username(username)
        self.page_input_password(password)
        self.page_click_login_btn()

