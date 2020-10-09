# coding=utf-8

import sys
import os
base_path = os.path.abspath(os.path.join(os.getcwd(), ".."))
sys.path.append(base_path)

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time
from business.mo_pro_business import Mo_Pro_Business
import requests
import json
import re
import requests.packages
import warnings
import allure
import pytest

url1 = 'https://shbweb.maxoffice.com/api/jointOffice/queryMoJointList'
header = {"Content-Type": "application/json"}


# @pytest.mark.skip(reason='跳过单独的TestClickEleTo类，会跳过类中所有方法')
@allure.feature('联合办公列表页')
class TestJoinList:

    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('https://shbweb.maxoffice.com/bangongshi/lianhe')
        cls.driver.maximize_window()

    def setup_method(self):
        self.rb = Mo_Pro_Business(self.driver)
        warnings.simplefilter("ignore", ResourceWarning)

    def teardown_method(self):
        pass

    def teardown_class(cls):
        cls.driver.close()

    def compare_result(self, api_data):

        # 忽略https的警告信息
        requests.packages.urllib3.disable_warnings()
        res2 = requests.request('post', url=url1, data=json.dumps(json.loads(api_data)), headers=header, verify=False)
        num = res2.json()['data']['total']

        if (self.rb.get_ele_exist('join_no_data')) is True:
            res1 = self.rb.get_ele('join_all_num')
            res1_num = re.sub('\D', '', res1)
            assert int(res1_num) == int(num)
        else:
            assert 0 == int(num)

    # 成功进入联合办公列表页
    @allure.story("进入联合办公列表页")
    def test_title_001(self):
        title = EC.title_contains("上海联合共享办公空间租赁")(self.driver)
        assert title is True

    data = [
            ('join_contryid_click', '{"page":1,"pageSize":20,"addressId":310104,"type":0,"featureIds":[],"cityId":310100}'),
            ('join_businessid_click', '{"page":1,"pageSize":20,"addressId":310104,"businessId":2223,"type":0,"featureIds":[],"cityId":310100}'),
            ('join_subway_click', ''),
            ('join_subwayid_click', '{"page":1,"pageSize":20,"metroId":68,"type":0,"featureIds":[],"cityId":310100}'),
            ('join_subwaystationid_click', '{"page":1,"pageSize":20,"metroId":68,"subwayId":840,"type":0,"featureIds":[],"cityId":310100}'),
            ('join_subway_all_click', ''),
            ('join_area_click', '{"page":1,"pageSize":20,"areaMax":500,"areaMin":300,"type":0,"featureIds":[],"cityId":310100}'),
            ('join_area_buxian_click', ''),
            ('join_people_click', ''),
            ('join_nump_click', '{"page":1,"pageSize":20,"numBerMax":15,"numBerMin":8,"type":0,"featureIds":[],"cityId":310100}'),
            ('join_nump_buxian_click', ''),
            ('join_price_click', '{"page":1,"pageSize":20,"priceMax":1500,"priceMin":800,"type":0,"featureIds":[],"cityId":310100}'),
            ('join_price_buxian_click', ''),
            ('join_fixtures_click', '{"page":1,"pageSize":20,"decorate":"简单装修","type":0,"featureIds":[],"cityId":310100}'),
            ('join_fixtures_buxian_click', ''),
            ('join_brand_click', '{"page":1,"pageSize":20,"type":0,"featureIds":[],"jointBrandId":2,"cityId":310100}'),
            ('join_brand_buxian_click', ''),
            ('join_clear_all', '{"page":1,"pageSize":20,"type":0,"featureIds":[],"cityId":310100}')
            ]

    # 点击查询条件
    @pytest.mark.parametrize("key,api_data", data)
    @allure.story("点击查询条件")
    def test_click_elements_002(self, key, api_data):

        res = self.rb.check_ele_click(key)
        if res:
            time.sleep(2)
            if api_data:
                self.compare_result(api_data)
            else:
                pass
        else:
            print('点击元素出错！！！！')

    # 搜索
    @allure.story("搜索-办伴")
    def test_queriy_es_003(self):

        res = self.rb.input_content('join_queriy_content', '办伴', 'join_queriy_click')
        if res:
            api_data = '{"page":1,"pageSize":20,"queryName":"办伴","type":0,"cityId":310100}'
            self.compare_result(api_data)
        else:
            print('搜索报错！！！！')
