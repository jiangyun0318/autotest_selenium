# coding=utf-8
from handle.mo_retaine_handle import Mo_Retaine_Handle
import time
import allure
import pytest


class Mo_Retaine_Business(object):
    def __init__(self, driver):
        self.mo_retaine_h = Mo_Retaine_Handle(driver)

    # 输入的手机号不正确
    def input_mobile_error(self, key, mobile, key1, key2):
        try:
            self.mo_retaine_h.input_mobile_content(key, mobile)
            time.sleep(4)
            self.mo_retaine_h.click_retaine_button(key1)
            time.sleep(4)
            self.mo_retaine_h.get_ele_text(key2)
            return True
        except:
            return False

    # 正常留资
    def input_mobile_True(self, key, mobile, key1, content, key2):
        try:
            with allure.step('输入需求内容'):
                self.mo_retaine_h.input_requests_content(key1, content)
                time.sleep(2)
            with allure.step('输入手机号'):
                self.mo_retaine_h.input_mobile_content(key, mobile)
                time.sleep(2)
            with allure.step('点击立即委托'):
                self.mo_retaine_h.click_retaine_button(key2)
            return True
        except:
            return False
