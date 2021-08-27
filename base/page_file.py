#!/usr/bin/env python
# -*-coding:utf-8 -*-
# @author:Gemini
# @time:  2021/8/20:17:54
# @email: 13259727865@163.com
import yaml

from base.log_config import root_log


class File(object):

    def read_yaml(self,path):
        """
        :param path: 要读取的yaml文件的路径
        :return: 读取到的数据（python类型）
        """
        root_log.info(f'read{path}')
        with open(path,"r",encoding="utf-8") as file:
            yamlfile = yaml.safe_load(file)
            root_log.info(f'return {yamlfile}')
            return yamlfile




