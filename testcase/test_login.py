#!/usr/bin/env python
# -*-coding:utf-8 -*-
# @author:Gemini
# @time:  2021/7/19:15:18
# @email: 13259727865@163.com
from selenium.webdriver.common.by import By

from front.admin_page import AdminPage


class TestLogin:
    def setup(self):
        self.main = AdminPage()


    def test_login1(self):
        self.main.go_login().phone_login('13259727865')
        huakuai = self.main.find(By.CLASS_NAME, "el-icon-d-arrow-right")
        # main.move_to_gap(huakuai,main.get_track(200))
        self.main.move_to_gap2(huakuai)