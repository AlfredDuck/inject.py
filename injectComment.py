#coding=utf-8


import time
import urllib
import urllib2
import cookielib



def useCookieToInject(text, n):
    #创建MozillaCookieJar实例对象
    cookie = cookielib.MozillaCookieJar()
    #从文件中读取cookie内容到变量
    cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
    #利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
    handler = urllib2.HTTPCookieProcessor(cookie)
    #通过handler来构建opener
    opener = urllib2.build_opener(handler)

    # 插曲：随机选择验证码？

    #post的参数
    values = {"rv_comment":text,
              "ck":"aSyc",                          #这里的ck代表cookie，每个账号不一样
              "start":"0",
              "submit_btn":"加上去",
              "captcha-solution":"damage",
              "captcha-id": "WlrpdoeT5LS6YLO06Kfy9Ot3:en"
              # 后面两个是验证码
              }
    data = urllib.urlencode(values)

    # 从文件读取帖子id
    arr = []
    f = open('tiezi.txt')
    num = f.readlines()                 # 逐行读取文件，并生成数组
    for item in num:
        item = item.strip('\n')           # 去掉换行符
        item = 'https://www.douban.com/group/topic/' + item + '/add_comment#last'
        print item                      # 后面跟 ',' 将忽略换行符
        arr.append(item)
    f.close()

    for url in arr:
        #创建请求的request
        request = urllib2.Request(url, data)

        #此处的open方法同urllib2的urlopen方法，也可以传入request
        response = opener.open(request)

        #打印获取的网页
        # print response.read()
        print '继续注入...'

        # 等待一段时间
        time.sleep(50)
    print '本次注入完成!'

    #写入log做记录
    foo = open('log.txt', 'a')                            # r 是只读（默认的），w、wb分别是写入文本&二进制，a 是追加
    now = time.localtime(time.time())                     # 获取当前的本地时间
    now = time.strftime('%m月%d日 %H:%M:%S', now)          # 将时间格式化一下
    foo.write(now + '\n' + '(' + str(n) + ') ' + text + '\n')     # str()将数字转字符串
    foo.close()


def readTeXT(n):
    f = open('taici.txt')
    lines = f.readlines()                   # 逐行读取文件，并生成数组
    print n, ' = ', lines[n]                # 后面跟 ',' 将忽略换行符
    useCookieToInject(lines[n], n)          # 调用cookie注入函数
    f.close()



if __name__ == '__main__':
    # 定时器（循环 + 间隔）
    i = 0
    while True:
        # 读取电影台词
        readTeXT(i)
        i = i + 1
        time.sleep(60*10)                       # 这里的sleep参数是 n 秒
        if i >= 45:                             # 暂时只有这么多台词
            print 'a loop has finished'
            i = 0                               # 重新开始一个循环





# cookie.txt
# .douban.com TRUE    /   FALSE   1462694897  bid "Y6FW5e3xrVI"
# .douban.com TRUE    /   FALSE       ck  "EXKS"
# .douban.com TRUE    /   FALSE       dbcl2   "88207952:DCprgKAMXkM"
# .douban.com TRUE    /   FALSE   1462694897  ue  "zhaoyingzong@gmail.com"




