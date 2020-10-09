# coding=utf-8

from base.find_element import FindElement


class Mo_Retaine_Page(object):
    def __init__(self, driver):
        self.fd = FindElement(driver)

    # 获取手机号不正确元素
    def get_mobile_error_element(self, key):
        return self.fd.get_element(key)

    # 获取输入手机号的元素
    def get_mobile_element(self, key):
        return self.fd.get_element(key)

    # 获取输入客户需求的元素
    def get_requests_element(self, key):
        return self.fd.get_element(key)

    # 获取立即委托按钮元素
    def get_retaine_click_element(self, key):
        return self.fd.get_element(key)
