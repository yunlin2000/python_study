# 引入要用到的第三方工具
import requests #爬取网页源码工具
import re   #正则表达式，解析网页源代码工具
import csv  #csv文件工具

# 要获取的网页URL地址
url = "https://movie.douban.com/top250"

# 伪装成浏览器
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

# 要装载的url参数
params={
    "start": 0,
    "filter": ""
}

# 获取目标网页源代码
resp = requests.get(url,params=params,headers=headers)

# 测试获取结果
print(resp.status_code)    #结果为200，则OK！

# 解析网页源代码获取数据
# 1.预装载正则表达式
obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<title>.*?)'
                 r'</span>.*?<br>(?P<year>.*?)&nbsp;/&nbsp;'
                 r'.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>'
                 r'.*?<span>(?P<num>.*?)人评价</span>',re.S)
result = obj.finditer(resp.text)
print(result)
# 保存数据到data.csv文件
f = open("./data.csv",mode="w")
csvwriter = csv.writer(f)
for it in result:
    # print(it.group("title"),it.group("year").strip(),it.group("score"),it.group("num"))
    dic = it.groupdict()
    dic["year"] = dic["year"].strip()
    csvwriter.writerow(dic.values())
f.close()
print("over!")

# data.csv文件问什么有空行？

