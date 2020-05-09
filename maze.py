# -*- coding:utf-8 -*-
from selenium import webdriver

# 打开并跳转百度页面
driver = webdriver.Chrome('http://www.mazegenerator.net/')

driver.get("https://www.baidu.com/")
