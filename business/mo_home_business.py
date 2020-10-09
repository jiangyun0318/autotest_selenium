# coding=utf-8
from handle.mo_home_handle import MoHandle
import time


class MoBusiness(object):
    def __init__(self, driver):
        self.mo_h = MoHandle(driver)

    # 页面某个元素是否存在
    def check_ele_exist(self, key, expect):
        ex = self.mo_h.get_ele_text(key)
        if ex == expect:
            return True
        else:
            print(ex)
            return False

    # 页面元素是否存在
    def check_ele_exist1(self, key):
        try:
            self.mo_h.get_ele_text(key)
            return True
        except:
            return False

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
