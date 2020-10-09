# coding=utf-8
from handle.mo_pro_handle import Mo_Pro_Handle
import time


class Mo_Pro_Business(object):
    def __init__(self, driver):
        self.mo_h = Mo_Pro_Handle(driver)

    # 点击页面元素
    def check_ele_click(self, key):
        try:
            self.mo_h.get_ele_click(key)
            return True
        except:
            return False

    # 输入框输入，然后点击
    def input_content(self, key, content, queiry):
        try:
            self.mo_h.send_queiry_content(key, content)
            time.sleep(3)
            self.mo_h.click_queiry_content(queiry)
            return True
        except:
            return False

    # 页面元素
    def get_ele(self, key):
        return self.mo_h.get_ele_text(key)

    # 页面元素
    def get_ele_exist(self, key):
        try:
            self.mo_h.get_ele_text(key)
            return True
        except:
            return False
