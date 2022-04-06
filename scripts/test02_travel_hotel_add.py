import pytest

import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.read_yaml import read_yaml


class TestHotelAdd:
    def setup_class(self):
        driver = GetDriver.get_web_driver(page.url_mis)
        self.page_in = PageIn(driver)
        self.page_in.page_get_PageTravelLogin().page_travel_login_success()
        self.hotel_add = self.page_in.page_get_PageTravelHotelAdd()


    def teardown_class(self):
        GetDriver.quit_web_driver()

    @pytest.mark.parametrize("hotel_add_name,hotel_add_price,expect", read_yaml("travel_hotel_add.yaml"))
    def test_travel_hotel_add(self, hotel_add_name, hotel_add_price, expect):
        self.hotel_add.page_travel_hotel_add(hotel_add_name, hotel_add_price)

        info = self.hotel_add.page_get_info()

        try:
            assert expect == info

        except Exception as e:
            print("错误原因：", e)

            self.hotel_add.base_get_img()

            raise