# coding=utf-8

import sys
import os
base_path = os.path.abspath(os.path.join(os.getcwd(), ".."))
sys.path.append(base_path)

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time
from business.mo_home_business import MoBusiness
import allure
import pytest


# @pytest.mark.skip(reason='跳过单独的TestShouYe类，会跳过类中所有方法')
@allure.feature('首页')
class TestShouYe:

    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('https://shbweb.maxoffice.com/')
        cls.driver.maximize_window()
        time.sleep(3)

    def setup_method(self):
        self.rb = MoBusiness(self.driver)
        self.window_before = self.driver.window_handles[0]
        self.driver.switch_to.window(self.window_before)

        if self.driver.current_url != 'https://shbweb.maxoffice.com/':
            self.driver.get('https://shbweb.maxoffice.com/')
            self.driver.refresh()
            time.sleep(2)

    def teardown_method(self):
        pass

    def teardown_class(cls):
        cls.window_before = cls.driver.window_handles[0]
        cls.driver.switch_to.window(cls.window_before)
        cls.driver.close()

    # 成功进入首页
    @allure.story("成功进入首页")
    def test_title_001(self):
        title = EC.title_contains("堂堂办公")(self.driver)
        assert title is True

    data = ['sy_remen', 'sy_brand', 'sy_property', 'sy_bgshi']

    # 检查页面元素
    # @pytest.mark.skip(reason='跳过 检查页面元素 方法')
    @allure.story("检查页面元素")
    @allure.description('检查页面元素是否存在的用例')
    @pytest.mark.parametrize("key", data)
    def test_group_elements_002(self, key):

        title = self.rb.check_ele_exist1(key)
        assert title is True

    data1 = [('sy_remen_click', 'xiezilou_element'),
             ('type_of_join', 'lianban_element'),
             ('type_of_off', 'bgshi_element'),
             ('type_of_pro', 'property_element'),
             ('type_of_map', 'map_element')
             ]

    # 定位元素+点击（不跳转新页面）
    @allure.story("定位元素+点击(不跳转新页面)")
    @pytest.mark.parametrize("key, expect_value", data1)
    def test_click_elements_003(self, key, expect_value):

        time.sleep(2)
        res = self.rb.check_ele_click(key)

        assert res is True

        if res:
            time.sleep(2)
            expect_res = self.rb.check_ele_exist1(expect_value)
            assert expect_res is not None
        else:
            print('点击元素报错！！！！')

    data2 = [
            ('sy_brand_click', 'brand_element'),
            ('sy_lianban_click', 'lianban_element'),
            ('sy_property_click', 'property_element'),
            ('sy_bgshi_click', 'bgshi_element'),
            ('sy_zixun_click', 'zixun_element')
            ]

    # 定位元素+点击（跳转新页面）
    @allure.story("定位元素+点击(跳转新页面)")
    @pytest.mark.parametrize("key, expect_value", data2)
    def test_click_elements_004(self, key, expect_value):

        time.sleep(2)
        res = self.rb.check_ele_click(key)

        assert res is True

        if res:
            # 切换最新的窗口
            windows_new = self.driver.window_handles  # 获得当前浏览器所有窗口
            self.driver.switch_to.window(windows_new[-1])  # 切换到最新打开窗口
            time.sleep(2)

            expect_res = self.rb.check_ele_exist1(expect_value)
            self.driver.close()

            assert expect_res is True

        else:
            print('点击元素报错！！！！')

    # 搜索框输入+点击
    @allure.story("搜索框输入+点击")
    def test_click_input_elements_005(self):

        res = self.rb.input_content("content", "徐家汇", "queiry")
        time.sleep(3)
        assert res is True

    data3 = [
             ('more_service_element', 'place_element', 'place_element_check'),
             ('more_service_element', 'business_element', 'business_element_check'),
             ('more_service_element', 'space_element', 'space_element_check'),
             ('more_service_element', 'through_element', 'through_element_check'),
             ('more_service_element', 'service_element', 'service_element_check')
             ]

    @allure.story("更多服务")
    @pytest.mark.parametrize("key, key1, expect_value", data3)
    def test_more_service_006(self, key, key1, expect_value):

        time.sleep(2)
        res = self.rb.check_ele_click(key)
        if res:
            time.sleep(2)
            res1 = self.rb.check_ele_click(key1)

            if res1:
                time.sleep(4)
                expect_res = self.rb.check_ele_exist1(expect_value)
                assert expect_res is True
