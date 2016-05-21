#coding=utf-8


import cookielib
import urllib2
import urllib
#关系：CookieJar —-派生—->FileCookieJar  —-派生—–>MozillaCookieJar和LWPCookieJar

# #声明cookie的存储路径
# filename = 'cookie.txt'

# #声明一个MozillaCookieJar对象实例来保存cookie,并写入文件
# cookie = cookielib.MozillaCookieJar(filename)

# #利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
# handler = urllib2.HTTPCookieProcessor(cookie)

# #通过handler来构建opener
# opener = urllib2.build_opener(handler)

# #此处的open方法同urllib2的urlopen方法，也可以传入request
# response = opener.open('http://www.douban.com')

# #保存Cookie到文件
# cookie.save(ignore_discard=True, ignore_expires=True)

# #打印Cookie
# for item in cookie:
#     print 'Name = '+item.name
#     print 'Value = '+item.value



#声明cookie的存储路径
filename = 'cookie.txt'

#声明一个MozillaCookieJar对象实例来保存cookie,并写入文件
cookie = cookielib.MozillaCookieJar(filename)

#利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler = urllib2.HTTPCookieProcessor(cookie)

#通过handler来构建opener
opener = urllib2.build_opener(handler)

#登录参数
values = {"form_email":"zhaoyingzong@gmail.com", 
          "form_password":"eric61746174",
          # "captcha-solution":"river",
          # "captcha-id": "Au9vIH0GLPdcjstcQXJ5jTo0:en"
          # 后面两个是验证码
          }
data = urllib.urlencode(values)

#登录url
url = "https://accounts.douban.com/login"

#声明request
request = urllib2.Request(url,data)

#此处的open方法同urllib2的urlopen方法，也可以传入request
response = opener.open(request)

#保存Cookie到文件
cookie.save(ignore_discard=True, ignore_expires=True)

#
print response.read()

#打印Cookie
for item in cookie:
    print 'Name = '+item.name
    print 'Value = '+item.value




