#!/usr/bin/env python
# -*-coding:utf-8 -*-
# @author:Gemini
# @time:  2021/7/14:15:14
# @email: 13259727865@163.com
from time import sleep

from selenium.webdriver.common.by import By

from base.page import BasePage
from front.login_main import LoginMain


class Login(BasePage):
    def phone_login1(self):
        self.find(By.CLASS_NAME, "el-input__inner").send_keys(13259727865)
        huakuai = self.find(By.CLASS_NAME, "el-icon-d-arrow-right")
        # main.move_to_gap(huakuai,main.get_track(200))
        self.move_to_gap2(huakuai)
        self.find(By.CLASS_NAME,"el-input-group__append").click()
        sleep(3)
        print("没有什么")
        self.find(By.XPATH, "//*[@id='app']/div/div[2]/div/form/div[1]/div[3]/div/div[1]/input").send_keys(1234)
        self.find(By.XPATH,"//*[@class='btn-box'][1]").click()
        # return LoginMain(self._driver)
        return LoginMain(self._driver)



