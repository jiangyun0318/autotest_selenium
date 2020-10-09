# coding=utf-8

import sys
import os

base_path = os.path.abspath(os.path.join(os.getcwd(), ".."))
sys.path.append(base_path)

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time
import allure
from business.mo_retaine_business import Mo_Retaine_Business
import pytest


# @pytest.mark.skip(reason='跳过单独的TestEntrustToLease类，会跳过类中所有方法')
@allure.feature('委托出租')
class TestEntrustToLease:

    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('https://shbweb.maxoffice.com/weituochuzu')
        cls.driver.maximize_window()
        time.sleep(2)

    def setup_method(self):
        self.rb = Mo_Retaine_Business(self.driver)

    def teardown_method(self):
        pass

    def teardown_class(cls):
        cls.driver.close()

    # 成功进入委托找房页面
    @allure.story("进入委托找房页面")
    def test_title_001(self):
        title = EC.title_contains("房源发布")(self.driver)
        assert title is True

    # 输入错误手机号
    @allure.story("输入错误手机号")
    def test_input_mobile_error_002(self):
        mobile_error = self.rb.input_mobile_error('mobile_entrust_lease', '1560000000', 'mobile_entrust_lease_button',
                                                  'mobile_entrust_lease_error')
        assert mobile_error is True

    # 输入成功的手机号，并立即委托成功
    @allure.story("输入成功的手机号，并立即委托成功")
    def test_input_mobile_success_003(self):
        retaine_success = self.rb.input_mobile_True('mobile_entrust_lease', '15688888888', 'requests_user_lease',
                                                    '城隍庙，160平，精装修，靠近地铁', 'mobile_entrust_lease_button')
        assert retaine_success is True
