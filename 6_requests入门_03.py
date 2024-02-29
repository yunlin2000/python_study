#引入第三方工具库
import requests

#准备好目标网址
url="https://movie.douban.com/j/chart/top_list"

#重新封装参数：params
params = {
    "type": "24",
    "interval_id": "100:90",
    "action": "",
    "start": 0,
    "limit": 20
}
#伪装成浏览器
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}


# 模拟浏览器访问网页

resp = requests.get(url,headers=headers,params=params)
print(resp.status_code)

print(resp.json())

with open("myhtml.txt","w",encoding="utf-8") as f:
    f.write(resp.text)
print("save OK!")

resp.close()   #关掉response，否则，请求太多会产生堵死问题
