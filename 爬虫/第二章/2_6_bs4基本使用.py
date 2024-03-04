#模块安装
# pip install bs4 -i 清华源

# 1. 拿到网页源代码
# 2. 用bs4解析，拿到数据

import requests
from bs4 import BeautifulSoup

import csv




# 网页url
url = "http://www.xinfadi.com.cn/getPriceData.html"

# post参数
data={
    "limit": 20,
    "current": 9,
    "pubDateStartTime": None,
    "pubDateEndTime": None,
    "prodPcatid": None,
    "prodCatid": None,
    "prodName": ""
}

# 获取网页源码
resp = requests.post(url,data=data)


# print(resp.json())
json_data = resp.json()["list"]
# 解析数据
# 1.把页面源代码交给SeatifulSoup进行处理，生成bs对象
page = BeautifulSoup(resp.text,features="html.parser")   #指定html解析
# 2.从bs对象中查找数据
# find(标签，属性=值)       找第一个标签
# find_all(标签，属性=值)   找所有标签
# 写入文件price.csv

f = open("./price.csv","w")
csvwriter = csv.writer(f)

csvwriter.writerow(json_data[0].keys())      #写入表头
for item in json_data:
    csvwriter.writerow(item.values())
    
    
print("saving over!")
f.close()