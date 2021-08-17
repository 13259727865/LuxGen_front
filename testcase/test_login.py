#!/usr/bin/env python
# -*-coding:utf-8 -*-
# @author:Gemini
# @time:  2021/7/19:15:18
# @email: 13259727865@163.com
from time import sleep

from selenium.webdriver.common.by import By

from front.main_page import MainPage


class TestLogin:
    def setup(self):
        self.main = MainPage()


    def test_login1(self):
        a = self.main.go_login().phone_login1()
        sleep(5)
        self.main.find(By.CLASS_NAME,a.history_locator)




