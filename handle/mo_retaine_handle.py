# coding=utf-8
from page.mo_retaine_page import Mo_Retaine_Page
from log.user_log import UserLog


class Mo_Retaine_Handle(object):

    def __init__(self,driver):
        self.driver = driver
        self.retaine_p = Mo_Retaine_Page(self.driver)
        get_user_log = UserLog()
        self.loger = get_user_log.get_log()

    # 获取页面手机号不正确内容
    def get_ele_text(self, key):
        return self.retaine_p.get_mobile_error_element(key).text

    # 输入留资的手机号码
    def input_mobile_content(self, key, content):
        self.loger.info("输入的手机号为：" + content)
        self.retaine_p.get_mobile_element(key).send_keys(content)

    # 输入留资的手机号码
    def input_requests_content(self, key, content):
        self.loger.info("输入用户需求为：" + content)
        return self.retaine_p.get_requests_element(key).send_keys(content)

    # 点击立即委托按钮
    def click_retaine_button(self, key):
        print('wwww', self.retaine_p.get_retaine_click_element(key))
        self.retaine_p.get_retaine_click_element(key).click()
