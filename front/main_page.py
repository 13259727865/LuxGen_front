#!/usr/bin/env python
# -*-coding:utf-8 -*-
# @author:Gemini
# @time:  2021/7/14:14:57
# @email: 13259727865@163.com
from selenium.webdriver.common.by import By

from base.page import BasePage
from front.login import Login


class MainPage(BasePage):
    _page_url = "http://test.simulation.luxcreo.cn/#/index"
    def go_login(self):
        self.find(By.CLASS_NAME,"login_btn").click()
        return Login(self._driver)


