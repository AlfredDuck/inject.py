#coding=utf-8

import cookielib
import urllib2
import urllib

 
# #创建MozillaCookieJar实例对象
# cookie = cookielib.MozillaCookieJar()

# #从文件中读取cookie内容到变量
# cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)

# #创建请求的request
# req = urllib2.Request("http://www.douban.com")

# #利用urllib2的build_opener方法创建一个opener
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

# #此处的open方法同urllib2的urlopen方法，也可以传入request
# response = opener.open(req)

# #打印获取的网页
# print response.read()



#创建MozillaCookieJar实例对象
cookie = cookielib.MozillaCookieJar()

#从文件中读取cookie内容到变量
cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)

#利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler = urllib2.HTTPCookieProcessor(cookie)

#通过handler来构建opener
opener = urllib2.build_opener(handler)

#post的参数
values = {"rv_comment":"upupup",
          "ck":"LnoU",                    #这里的ck代表cookie，每个账号不一样
          "start":"300",
          "submit_btn":"加上去"}
data = urllib.urlencode(values)

#post请求的url
url = "http://www.douban.com/group/topic/52622604/add_comment#last"

#创建请求的request
request = urllib2.Request(url, data)

#此处的open方法同urllib2的urlopen方法，也可以传入request
response = opener.open(request)

#打印获取的网页
print response.read()







