import requests
import re
import csv


# 目标网页地址url
url = "https://www.dytt89.com/"

# 伪装成浏览器
headers={
   "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
# 获取网页源代码
resp1 = requests.get(url,headers=headers,verify=False)
resp1.encoding="gbk"
print(resp1.text)

f = open("./downlist.csv",mode="w",encoding="gbk")
csvwriter = csv.writer(f)

# 解析出需要的数据
# 预定义正则表达式
obj1 = re.compile(r'2024必看热片.*?<ul>(?P<ul>.*?)</ul>',re.S)
result1 = obj1.search(resp1.text)
ul = result1.group("ul")
# print(ul)
resp1.close()   #关闭keeplive线程
# 进一步解析数据
# # 预定义正则
obj2 = re.compile(r"<li><a href='(?P<href>.*?)'",re.S)
result2=obj2.finditer(ul)
child_href_list = []
for itt in result2:
    child_href = url + itt.group("href").strip("/")
    # print(child_hre.f)
    child_href_list.append(child_href)
# print(child_href_list)
# # 预定义正则
obj3 = re.compile(r'◎片　　名(?P<movie_name>.*?)<br />.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<download>.*?)">',re.S)

for item in child_href_list:
    resp2 = requests.get(item,headers=headers,verify=False)
    resp2.encoding="gbk"
    # print(resp2.text)
    # break
    result3 = obj3.search(resp2.text)
    # print(result3.group("movie_name"),result3.group("download"))
    dic = result3.groupdict()
    csvwriter.writerow(dic.values())
    resp2.close()
f.close()

# 保存的数据文件：downlist.csv文件内容乱码？？？？？，在notepad和excel中打开不会乱码。