#!/usr/bin/env python
# -*-coding:utf-8 -*-
# @author:Gemini
# @time:  2021/7/14:14:57
# @email: 13259727865@163.com
from selenium.webdriver.common.by import By

from base.page import BasePage
from base.page_file import File
from front.login import Login


class MainPage(BasePage):
    # _page_url = "http://test.simulation.luxcreo.cn/#/index"
    _page_url = File().read_yaml(path="../config/url.yaml")["url"]
    def go_login(self):
        # self.find("class name","login_btn").click()
        self.parse_action("../yaml/main.yaml","go_login")
        return Login(self._driver)


