#!/usr/bin/env python
# -*-coding:utf-8 -*-
# @author:Gemini
# @time:  2021/7/14:15:14
# @email: 13259727865@163.com
from selenium.webdriver.common.by import By

from base.page import BasePage


class Login(BasePage):
    def phone_login(self,phone):
        self.find(By.CLASS_NAME, "el-input__inner").send_keys(phone)



