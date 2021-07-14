#!/usr/bin/env python
# -*-coding:utf-8 -*-
# @author:Gemini
# @time:  2021/7/14:14:00
# @email: 13259727865@163.com
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    _page_url = ""

    def __init__(self,driver: WebDriver = None):
        if driver is None:
            option = Options()
            option.debugger_address = '127.0.0.1:9222'
            self._driver = webdriver.Chrome(options=option)
        else:
            self._driver = driver
        if self._page_url != "":
            self._driver.get(self._page_url)

    def find(self,by,locator):
        self._driver.find_element(by,locator)

