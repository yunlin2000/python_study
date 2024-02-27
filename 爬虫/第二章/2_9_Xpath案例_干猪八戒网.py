"""
思路：
    1、拿到页面源代码
    2、提取和解析数据
    //*[@id="__layout"]/div/div[3]/div/div[4]/div/div[2]/div[1]/div[1]
"""

import requests
from lxml import etree

url="https://www.zbj.com/fw/?k=saas&lr=3374&r=10"
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
         }

resp=requests.get(url,headers=headers)
print(resp.headers.get("content-type"))
# print(resp.text)
with open("myhtml.txt","w",encoding="utf-8") as f:
    f.write(resp.text)

html = etree.HTML(resp.text)

#xpath:/html/body/div[2]/div/div/div[3]/div/div[4]/div/div[2]/div[1]/div[1]/div/div[3]/div[2]/a

div_list= html.xpath("//*[@id='__layout']/div/div[3]/div/div[4]/div/div[2]/div[1]/div")
print(div_list)
for div in div_list:
    price=div.xpath("./div/div[3]/div[1]/span/text()")[0].strip("¥")
    title="".join(div.xpath("./div/div[3]/div[2]//text()"))
    com_name=div.xpath("./div/a/div[2]/div[1]/div/text()")[0]
    print(price,title,com_name)
