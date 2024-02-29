"""
requests第三方库：模拟浏览器，向服务器发送请求，获得服务器响应结果
1.requests.requests方法
 requests.request(method, url, **kwargs)
(1). method - 请求方式

    序号 方式 含义

    1 ‘GET’ 请求获取URL位置的资源

    2 ‘HEAD’ 请求获取URL位置资源的响应消息报告，即获得资源的头部信息

    3 ‘POST’ 请求向URL位置的资源附加新的消息

    4 ‘PUT’ 请求向URL位置存储一个资源，覆盖原URL位置的资源

    5 ‘PATCH’ 请求局部更新URL位置的资源，即改变该处资源部分内容

    6 ‘DELETE’ 请求删除URL位置存储的资源

    通过URL和命令管理资源，操作独立无状态，网络通道及服务器成了黑盒子。

(2). url - 待操作页面的主链接
(3). **kwargs - 访问控制参数(可选)

    序号 方式 使用对象 说明

    1 params= 字典或字节序列 向服务器请求数据时使用，作为参数增加到请求网址-url后部分中

    2 data= 字典、字节序列或文件对象 向服务器提交数据时使用，data的内容因安全问题，不会直接放在URL链接里，而是放在请求体内

    3 json= JSON格式的数据 和data类似，作为请求体向服务器提交

    4 headers= 字典 为HTTP定制请求头。可定制User-Agent和Cookie等请求头信息，模拟浏览器内核等

    5 cookies= 字典或者cookieJar 为HTTP定制cookie

    6 auth= 元组 HTTP认证功能

    7 files= 字典 用于传输文件，存放到相应的URL上

    8 timeout= float或(start,end) 设定超时时间，在这个时间内没有返回结果，则抛出timeout异常

    9 proxies= 字典 分别为HTTP和HTTPS设定代理服务器，这样我们访问网页使用的IP地址就是代理服务器的IP地址，防止逆追踪。可增加登录认证

    10 allow_redirects= 布尔型 默认为1，表示是否允许重定向

    11 steam= 布尔型 默认为1，表示是否允许对获取的内容进行立即下载

    12 verify= 布尔型 默认为1，认证SSL证书开关

    13 cert= 元组 本地SSL证书路径

"""
import requests
# params参数使用示例
kw={
    "sort":"U",
    "range":"0,10",
    "tags":"2020,青春"
    }
response = requests.request("get","https://www.baidu.com",params=kw)

print("url of get method:",response.request.url)

# data参数使用示例
kw={
    "name":"li",
    "age":"22"
    }
response = requests.request("post","https://www.baidu.com",data=kw)
print("url of post method:",response.request.headers)
