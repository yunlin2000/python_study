# 准备工具 selenium pypiwin32
import datetime
import time

import win32com.client
from selenium import webdriver
from selenium.webdriver.common.by import By

speak = win32com.client.Dispatch("SAPI.SpVoice")

# 1.使用工具selenium帮我们打开目标网站
# 定义访问目标网址：www.taobao.com
url = 'https://www.taobao.com'
# 打开网站
driver = webdriver.Chrome()
driver.get(url)
time.sleep(3)
# 点击“亲，请登录”，进入登录页面
driver.find_element(By.LINK_TEXT, '亲，请登录').click()
print("请扫码登录！")
time.sleep(8)
driver.get('https://cart.taobao.com/cart.htm')
time.sleep(5)
# 点击 全选
while 1 == 1:
    if driver.find_element(By.ID, "J_SelectAll1"):
        driver.find_element(By.ID, "J_SelectAll1").click()
        break
# 写真正的秒杀逻辑代码
# 秒杀逻辑：获取当前互联网时间 秒杀：2024-01-15 16：00：00.000000(精确到纳秒级)
while 1 == 1:
    nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    print(nowTime)
    if nowTime >= '2024-01-15 16：15：00.000000':
        while 1 == 1:
            if driver.find_element(By.LINK_TEXT, "结 算"):
                driver.find_element(By.LINK_TEXT, "结 算").click()
                print("云霖主人你好，双11的茅台酒我已经抢到了，哈哈哈哈哈哈")
                speak.Speak('云霖主人你好，双11的茅台酒我已经抢到了，哈哈哈哈哈哈')
                break

time.sleep(50)
