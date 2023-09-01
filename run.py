# 1、导入库文件
from python_selenium import selenium_learn  # 导入函数文件
from test_data import test_data  # 导入测试数据文件
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
driver.implicitly_wait(10)

# 2、调用函数
# 1）将参数先取出来
url = test_data.url["url"]  # 调用某个函数里面的 某个元组
user = test_data.login_date["username"]
pwd = test_data.login_date["password"]
# 2） 传参
result = selenium_learn.search_key(driver=driver, url=url, username=user, password=pwd, By=By)

print(result)  # 打印的是一个队列

time.sleep(5)
