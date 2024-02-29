"""
正则表达式的概念： Regular Expression,一种使用表达式的方式对字符串进行匹配的语法规则。
    我们抓取到的网页源码本质上就是超长的字符串，想从里面提取内容，用正则再合适不过了。
    正则的语法：使用元字符进行排列组合匹配字符串，在线测试正则表达式工具网站（https://tool.oschina.net/regex/）  
    常用元字符：
    1.  .   匹配除换行符以外的任意字符（一个点就匹配一个字符）
    2.  \w  匹配字母，数字或下划线
    3.  \s  匹配任意的空白字符
    4.  \d  匹配数字
    5.  \n  匹配一个换行符
    6.  \t  匹配一个制表符

    7.  ^   匹配字符串的开始
    8.  $   匹配字符串的结尾

    9.  \W  匹配非字母，数字和下划线
    10. \D  匹配非数字
    11. \S  匹配非空白符
    12. a|b 匹配字符a或字符b
    13. ()  匹配括号内的表达式，也表示一个组
    14. [...]   匹配字符组中的字符
    15. [^...]  匹配除了字符组中字符之外的所有字符

    量词：控制前面的元字符出现的次数
    1.  *   重复零次或更多次
    2.  +   重复一次或更多次
    3.  ?   重复零次或一次
    4.  {n}  重复n次
    5.  {n,} 重复n次或更多次
    6.  {n,m}   重复n次到m次

    贪婪匹配和惰性匹配：
    1.  .*  贪婪匹配
    2.  .*? 惰性匹配
        这两个我们要重点说说，因为，用的最多的就是惰性匹配。


"""




#引入re正则表达式模块
import re

#1.findall:查找字符串中所有符合正则的内容，返回list
lst = re.findall(r"m","mai le fo len, mai ni mei!")
print(lst)    #['m','m','m']

lst = re.findall(r"\d*","5点前，你要给我5000万")
print(lst)

#惰性匹配和贪婪匹配
lst = re.findall(r".*?x","dfsdfsdfsdfsxeiiioiewifjdsifxueuiweioriuoeiuwrix")
print(lst)

lst = re.findall(r'<div class=".*?">.*?</div>', '<div class="jay">周杰伦</div><div class="jj">林俊杰</div>')
print(lst)

lst = re.findall(r"玩儿.*?游戏","玩儿吃鸡游戏，晚上一起上游戏，干嘛呢？打游戏啊")
print(lst)

lst = re.findall(r"玩儿.*游戏","玩儿吃鸡游戏，晚上一起上游戏，干嘛呢？打游戏啊")
print(lst)
#惰性匹配
lst =re.findall(r"<.*?>","<div>胡辣汤</div>")
print(lst)
#贪婪匹配
lst = re.findall(r"<.*>","<div>胡辣汤</div>")
print(lst)

#2.finditer:匹配字符串中所有符合正则的内容，返回迭代器。从迭代器中拿到内容需要.group(),迭代器的效率比列表高很多。
lst = re.findall(r"\d+","我的电话号码是：10086，我女朋友的电话是：10010")
print(lst)
it = re.finditer(r"\d+","我的电话号码是：10086，我女朋友的电话是：10010")
print(it)
for i in it:
    print(i.group())

#3.search：找到一个结果就返回，返回的结果是match对象。拿数据需要.group()
s = re.search("\d+","我的电话号码是：10086，我女朋友的电话是：10010")
print("search:",s.group())    #返回结果：10086

# #4.match:从头开始匹配
# s = re.match("\d+","10086，我女朋友的电话是：    10010")
# print("match:",s.group())        #返回结果10086

# #5.compile():可以将长长的正则表达式进行预加载，方便后面使用
# obj = re.compile("\d+")
# ret = obj.finditer("我的电话号码是：10086，我女朋友的电话是：10010")
# for it in ret:
#     print(it.group())

# lst = obj.findall("我就不信你不还我100000000")
# print(lst)

#6.正则中的内容如何单独提取？
# 单独获取到正则中的具体内容可以给分组起名字
s ="""
<div class='jay'><span id='1'>郭麒麟</span></div>
<div class='jj'><span id='2'>宋铁</span></div>
<div class='jolin'><span id='3'>大聪明</span></div>
<div class='sylar'><span id='4'>范思哲</span></div>
<div class='tory'><span id='5'>胡说八道</span></div>
"""
obj = re.compile(r"<div class='.*?'><span id='\d+'>.*?</span></div>",re.S)    #re.S:让“.”匹配换行符
result = obj.finditer(s)
for it in result:
    print(it.group())





