from time import sleep

import page
from base.base import Base


class PageTravelHotelAdd(Base):
    # 点击酒店管理
    def page_click_hotel_manage(self):
        sleep(1)
        self.base_click(page.travel_hotel_manage)

    # 点击酒店列表
    def page_click_hotel_list(self):
        self.base_click(page.travel_hotel_list)

    # 点击新增
    def page_click_add_btn(self):
        sleep(1)
        self.base_click(page.travel_hotel_add_btn)

    # 输入酒店名
    def page_input_hotel_name(self, hotel_add_name):
        sleep(1)
        self.base_input(page.travel_hotel_add_name, hotel_add_name)

    # 输入酒店价格
    def page_input_hotel_price(self, hotel_add_price):
        self.base_input(page.travel_hotel_add_price, hotel_add_price)

    # 点击确定按钮
    def page_click_confirm_btn(self):
        sleep(1)
        self.base_click(page.travel_hotel_add_confirm_btn)

    # 获取 增加提示信息
    def page_get_info(self):
        sleep(1)
        return self.base_get_text(page.travel_hotel_add_info)
        # sleep(1)

    # 组合增加酒店业务方法
    def page_travel_hotel_add(self, hotel_add_name, hotel_add_price):
        self.page_click_hotel_manage()
        self.page_click_hotel_list()
        self.page_click_add_btn()
        self.page_input_hotel_name(hotel_add_name)
        self.page_input_hotel_price(hotel_add_price)
        self.page_click_confirm_btn()
