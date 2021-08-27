#!/usr/bin/env python
# -*-coding:utf-8 -*-
# @author:Gemini
# @time:  2021/7/14:14:00
# @email: 13259727865@163.com

import os,sys
base_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(base_dir)
import time
from typing import List,Dict
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from page_file import *

class BasePage:
    """
        基础类，封装框架中常用方法
    """

    _page_url = ""  #url在子类中赋值

    def __init__(self,driver: WebDriver = None):
        if driver is None:
            # option = Options()
            # option.debugger_address = '127.0.0.1:9222'
            # self._driver = webdriver.Chrome(options=option)
            # option.add_argument('--headless')
            # self._driver = webdriver.Chrome(chrome_options=option)

            self._driver = webdriver.Chrome()
        else:
            self._driver = driver
        if self._page_url != "":
            self._driver.get(self._page_url)

    def find(self,by,locator): #查找元素
        return self._driver.find_element(by,locator)

    def find_click(self,by,locator):  #查找元素后点击
        return self._driver.find_element(by,locator).click()

    def find_sendkey(self,by,locator,keys):  #查找元素后输入keys
        return self._driver.find_element(by,locator).send_keys(keys)



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

    def move_to_gap(self,slider, tracks):
        """
        拉动滑块方法，slider是要移动的滑块,tracks是要传入的移动距离
        :param slider:
        :param tracks:
        :return:
        """
        ActionChains(self._driver).click_and_hold(slider).perform()
        for x in tracks:
            ActionChains(self._driver).move_by_offset(xoffset=x, yoffset=0).perform()
        time.sleep(0.5)
        ActionChains(self._driver).release().perform()

    def move_to_gap2(self,slider):
        """
        # 拉动滑块方法，slider是要移动的滑块
        :param slider: 移动的滑块元素
        :return:
        """
        ActionChains(self._driver).click_and_hold(slider).perform()
        ActionChains(self._driver).move_by_offset(xoffset=240, yoffset=0).perform()
        time.sleep(0.5)
        ActionChains(self._driver).release().perform()

    def parse_action(self,path,fun):
        """
        读取yaml文件中元素信息，操作方式,判断不同操作方式下的元素对其做出对应的操作
        :param path: yaml文件路径
        :param fun: 调用该方法的fun名称，对应yaml中的key
        :return:
        """
        yaml_file=File().read_yaml(path)
        steps: List[Dict] = yaml_file[fun]
        for step in steps:
            print(step)
            if step['action'] == 'find':
                root_log.info(f"action:find,by:{step['by']},locator:{step['locator']}")
                self.find(step['by'],step['locator'])
            elif step['action'] == 'find_click':
                root_log.info(f"action:find_click,by:{step['by']},locator:{step['locator']}")
                self.find_click(step['by'],step['locator'])
            elif step['action'] == 'sendkeys':
                root_log.info(f"action:sendkeys,by:{step['by']},locator:{step['locator']},keys:{step['sendkeys']}")
                self.find_sendkey(step['by'],step['locator'],step['sendkeys'])
            elif step['action'] == 'move_to_gap':
                root_log.info(f"action:move_to_gap,locator:{step['locator']}")
                self.move_to_gap2(step['locator'])
            else:
                # print("无该方法，请联系管理员！！")
                root_log.error("无该方法，请联系管理员添加！")
