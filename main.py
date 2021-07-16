#!/usr/bin/env python
# -*-coding:utf-8 -*-
# @author:Gemini
# @time:  2021/7/14:15:30
# @email: 13259727865@163.com
from selenium.webdriver.common.by import By

from front.admin_page import AdminPage

if __name__ == '__main__':
    main = AdminPage()
    main.go_login().phone_login('13259727865')
    huakuai =main.find(By.CLASS_NAME,"el-icon-d-arrow-right")
    # main.move_to_gap(huakuai,main.get_track(200))
    main.move_to_gap2(huakuai)