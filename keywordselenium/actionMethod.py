# coding=utf-8

from selenium import webdriver
from base.find_element import FindElement
import time


class ActionMethod:
    #打开浏览器
    def open_browser(self, browser):
        if browser == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'firefox':
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Edge()
        
    #输入地址
    def get_url(self,url):
        self.driver.get(url)
    
    #定位元素
    def get_element(self,key):
        find_element = FindElement(self.driver)
        element = find_element.get_element(key)
        return element

    def get_new_element(self, key):
        windows_new = self.driver.window_handles  # 获得当前浏览器所有窗口
        print('windows_new---->', windows_new)
        self.driver.switch_to.window(windows_new[-1])  # 切换到最新打开窗口

        find_element = FindElement(self.driver)
        element = find_element.get_element(key)

        time.sleep(2)
        self.driver.close()

        windows_new = self.driver.window_handles  # 获得当前浏览器所有窗口
        print('windows_new---->', windows_new)
        self.driver.switch_to.window(windows_new[0])  # 切换到最新打开窗口

        return element
    
    #输入元素
    def element_send_keys(self,value,key):
        element = self.get_element(key)
        element.send_keys(value)
    
    #点击元素
    def click_element(self,key):
        self.get_element(key).click()
    
    #等待
    def sleep_time(self):
        time.sleep(3)
    
    #关闭浏览器
    def close_browser(self):
        self.driver.close()
    
    #获取title
    def get_title(self):
        title = self.driver.title
        return title


act = ActionMethod()