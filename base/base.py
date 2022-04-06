import allure
from selenium.webdriver.support.wait import WebDriverWait

from tools.get_log import GetLog

log = GetLog.get_logger()

class Base:
    # 初始化
    def __init__(self, driver):
        log.info("正在初始化driver: {}".format(driver))
        """解决driver"""
        self.driver = driver

    # 查找 方法封装
    def base_find(self, loc, timeout=30, poll=0.5):
        """
        :param loc: 格式为列表或元祖， 内容：元素定位信息使用By类
        :param timeout: 查找元素超时时间， 默认30秒
        :param poll: 查找元素频率 默认为0.5
        :return: 元素
        """
        log.info("正在查找元素：{} ".format(loc))
        return (WebDriverWait(self.driver,
                              timeout=timeout,
                              poll_frequency=poll).until(lambda x: x.find_element(*loc)))

    # 输入 方法封装
    def base_input(self, loc, value):
        """
        :param loc: 元素的定位信息
        :param value: 要输入的值
        """
        # 1. 获取元素
        el = self.base_find(loc)
        # 2. 清空操作
        log.info("正在对：{} 元素执行清空操作！".format(loc))
        el.clear()
        # 3. 输入操作
        log.info("正在对：{} 元素执行输入：{} 操作！".format(loc, value))
        el.send_keys(value)

    # 点击 方法封装
    def base_click(self, loc):
        """
        :param loc:元素定位信息
        """
        log.info("正在对：{} 元素执行点击操作！".format(loc))
        # 获取元素并点击
        self.base_find(loc).click()

    # 获取 元素文本
    def base_get_text(self, loc):
        """
        :param loc:元素定位信息
        :return: 返回元素的文本值
        """
        text = self.base_find(loc).text
        log.info("正在对：{} 元素获取文本操作！获取的文本值为：{} ".format(loc, text))
        return text

    # 截图
    def base_get_img(self):
        log.error("断言出错，正在执行截图操作！")
        # 1.调用截图方法
        self.driver.get_screenshot_as_file("./image/err.png")
        log.error("断言出错，正在将错误图片写入allure报告！")
        # 2.调用图片写入报告方法
        self.__base_write_img()

    # 将图片写入报告方法 （私有）
    def __base_write_img(self):
        # 1.获取图片文件流
        # allure.attach(self.driver.get_screenshot_as_png, "./image/err.png", allure.attachment_type.PNG)
        with open("./image/err.png", "rb") as f:
            # 2. 调用allure.attach附加方法
            allure.attach(f.read(), "错误原因：", allure.attachment_type.PNG)
            # allure.attach("错误原因：", f.read(), allure.attachment_type.PNG)  在最新版 allure-pytest-2.9.45 中不能使用