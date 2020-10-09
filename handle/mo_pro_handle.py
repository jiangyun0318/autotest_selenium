# coding=utf-8
from page.mo_pro_page import Mo_Pro_Page
from log.user_log import UserLog


class Mo_Pro_Handle(object):
    def __init__(self,driver):
        self.driver = driver
        self.register_p = Mo_Pro_Page(self.driver)
        get_user_log = UserLog()
        self.loger = get_user_log.get_log()

    #获取页面元素内容
    def get_ele_text(self, key):
        return self.register_p.get_element_page(key).text

    # 获取页面元素点击
    def get_ele_click(self, key):
        return self.register_p.get_element_page(key).click()

    # 输入搜索框内容
    def send_queiry_content(self, key, content):
        self.loger.info("输入的搜索内容：" + content)
        return self.register_p.get_queiry_element(key).send_keys(content)

    # 搜索框元素点击
    def click_queiry_content(self, key):
        return self.register_p.get_queiry_click_element(key).click()

    #点击登录按钮
    def click_register_button(self):
        self.register_p.get_button_element().click()
