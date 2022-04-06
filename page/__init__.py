from selenium.webdriver.common.by import By
"""以下数据为旅游网后台管理系统url"""
# 后台管理url
url_mis = "http://localhost:8080/#/login"
"""以下数据为后台管理系统模块配置数据"""
# 用户名
travel_username = [By.CSS_SELECTOR, "[placeholder='请输入账号']"]
# 密码
travel_password = (By.CSS_SELECTOR, "[placeholder='请输入密码']")
# 登录按钮
travel_login_btn = (By.XPATH, "//*[@id='login']/form/div[3]/div/button")
# 系统主页
travel_home = (By.XPATH, "//*[@id='leftMenuId']/li[1]/div")
# 酒店管理
travel_hotel_manage = (By.XPATH, "//*[@id='leftMenuId']/li[2]/div")
# 酒店列表
travel_hotel_list = (By.XPATH, "//*[@id='leftMenuId']/li[2]/ul")
# 新增按钮
travel_hotel_add_btn = (By.XPATH, "//*[@id='app']/section/section/main/div/div[1]/form/div[2]/div/button[2]")
# 酒店名称
travel_hotel_add_name = (By.XPATH, "//*[@id='app']/section/section/main/div/div[4]/div/div[2]/form/div[1]/div/div/input")
# 酒店价格
travel_hotel_add_price = (By.XPATH, "//*[@id='app']/section/section/main/div/div[4]/div/div[2]/form/div[2]/div/div/input")
# 增加酒店确定按钮
travel_hotel_add_confirm_btn = (By.XPATH, "//*[@id='app']/section/section/main/div/div[4]/div/div[3]/div/button[2]")
# 增加提示信息
travel_hotel_add_info = (By.XPATH, "/html/body/div[2]/div/div[2]/div[1]/div[2]")
