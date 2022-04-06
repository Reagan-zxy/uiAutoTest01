from page.page_travel_hotel_add import PageTravelHotelAdd
from page.page_travel_login import PageTravelLogin


class PageIn:
    def __init__(self, driver):
        self.driver = driver

    # 获取PageTravelLogin对象
    def page_get_PageTravelLogin(self):
        return PageTravelLogin(self.driver)

    def page_get_PageTravelHotelAdd(self):
        return PageTravelHotelAdd(self.driver)



