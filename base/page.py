#!/usr/bin/env python
# -*-coding:utf-8 -*-
# @author:Gemini
# @time:  2021/7/14:14:00
# @email: 13259727865@163.com
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    _page_url = ""

    def __init__(self,driver: WebDriver = None):
        if driver is None:
            option = Options()
            # option.debugger_address = '127.0.0.1:9222'
            # self._driver = webdriver.Chrome(options=option)
            # option.add_argument('--headless')
            # self._driver = webdriver.Chrome(chrome_options=option)
            self._driver = webdriver.Chrome()
        else:
            self._driver = driver
        if self._page_url != "":
            self._driver.get(self._page_url)

    def find(self,by,locator):
        return self._driver.find_element(by,locator)

    def get_track(self,distance):  # distance为传入的总距离
        # 移动轨迹
        track = []
        # 当前位移
        current = 0
        # 减速阈值
        mid = distance * 4 / 5
        # 计算间隔
        t = 0.01
        # 初速度
        v = 10

        while current < distance:
            if current < mid:
                # 加速度为2
                a = 4
            else:
                # 加速度为-2
                a = -3
            v0 = v
            # 当前速度
            v = v0 + a * t
            # 移动距离
            move = v0 * t + 1 / 2 * a * t * t
            # 当前位移
            current += move
            # 加入轨迹
            track.append(round(move))
        return track

    def move_to_gap(self,slider, tracks):  # slider是要移动的滑块,tracks是要传入的移动轨迹
        ActionChains(self._driver).click_and_hold(slider).perform()
        for x in tracks:
            ActionChains(self._driver).move_by_offset(xoffset=x, yoffset=0).perform()
        time.sleep(0.5)
        ActionChains(self._driver).release().perform()

    def move_to_gap2(self,slider):  # slider是要移动的滑块,tracks是要传入的移动轨迹
        ActionChains(self._driver).click_and_hold(slider).perform()
        ActionChains(self._driver).move_by_offset(xoffset=240, yoffset=0).perform()
        time.sleep(0.5)
        ActionChains(self._driver).release().perform()

