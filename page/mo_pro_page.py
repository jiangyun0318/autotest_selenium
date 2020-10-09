# coding=utf-8

from base.find_element import FindElement


class Mo_Pro_Page(object):
    def __init__(self, driver):
        self.fd = FindElement(driver)

    # 获取页面元素
    def get_element_page(self, key):
        return self.fd.get_element(key)

    # 获取搜索框元素
    def get_queiry_element(self, key):
        return self.fd.get_element(key)

    # 获取搜索查询按键
    def get_queiry_click_element(self, key):
        return self.fd.get_element(key)

    # 获取登录按钮元素
    def get_button_element(self):
        return self.fd.get_element("login")
