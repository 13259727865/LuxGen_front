#!/usr/bin/env python
# -*-coding:utf-8 -*-
# @author:Gemini
# @time:  2021/7/19:15:18
# @email: 13259727865@163.com
from time import sleep

import pytest, allure
from selenium.webdriver.common.by import By

from front.main_page import MainPage

@allure.feature('登录功能')
class TestLogin:
    @allure.story('实例化')
    def setup(self):
        self.main = MainPage()

    @allure.feature('登录流程')
    def test_login1(self):
        a = self.main.go_login().phone_login1()
        sleep(5)
        with allure.step("确认查找历史记录元素，保证登录跳转成功"):
            self.main.find(By.CLASS_NAME,a.history_locator)
        assert True



if __name__ == '__main__':
    pytest.main(["--alluredir=./result"])