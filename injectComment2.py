#coding=utf-8


import re
import time
import urllib
import urllib2
import cookielib
from bs4 import BeautifulSoup as bs


import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )



# delete comment

def postDeleteRequest (cid, tiezi_id):
    #创建MozillaCookieJar实例对象
    cookie = cookielib.MozillaCookieJar()
    #从文件中读取cookie内容到变量
    cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
    #利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
    handler = urllib2.HTTPCookieProcessor(cookie)
    #通过handler来构建opener
    opener = urllib2.build_opener(handler)
    #post的参数
    values = {
        "cid": cid,
        "ck": "oE4f"                          #这里的ck代表cookie，每个账号不一样
    }
    data = urllib.urlencode(values)
    url = 'https://www.douban.com/j/group/topic/' + tiezi_id + '/remove_comment'

    #创建请求的request
    request = urllib2.Request(url, data)
    #此处的open方法同urllib2的urlopen方法，也可以传入request
    response = opener.open(request)
    #打印获取的网页 ({"r":0} means delete success)
    print response.read()



def deleteComment(tiezi_id):
    url = 'https://www.douban.com/group/topic/' + tiezi_id + '/'
    print url
    # 访问链接
    req = urllib2.Request(url)                 # 构造请求
    res = urllib2.urlopen(req, timeout=20)     # 发起请求并获得请求结果
    resText = res.read()                       # 结果转为文本格式

    # 解析article页面
    # 将网页内容转为soup对象，并指定解析方式
    soup = bs(resText, 'html.parser')

    # python 异常类型： http://www.cnblogs.com/rubylouvre/archive/2011/06/22/2086644.html
    try:
        comments = soup.find(id='comments')
        ps = comments.find_all('p')
        print 'kkkkk'
        for item in ps:
            if item.string == '++o( >﹏<。)┛++':
                print item
                result = item
        print result.parent.find(class_='lnk-reply')
        href = result.parent.find(class_='lnk-reply')['href']
        print href
    except StandardError:
        print '未找到需要删除的评论'
    except TypeError:
        print 'maybe get error'
    else:
        # 正则提取出评论id
        text = href
        pattern = re.compile('cid=(.*)#last')
        cid = pattern.search(text).group(1)
        print '要删除的评论id：', cid

        # step 2
        postDeleteRequest(cid=cid, tiezi_id=tiezi_id)



# inject comment
def injectComment(tiezi_id):

    # prepare for url and text
    text = '++o( >﹏<。)┛++'
    url = 'https://www.douban.com/group/topic/' + tiezi_id + '/add_comment#last'

    # use cookie to inject comment
    # 创建MozillaCookieJar实例对象
    cookie = cookielib.MozillaCookieJar()
    # 从文件中读取cookie内容到变量
    cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
    # 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
    handler = urllib2.HTTPCookieProcessor(cookie)
    # 通过handler来构建opener
    opener = urllib2.build_opener(handler)
    # 插曲：随机选择验证码？
    #post的参数
    values = {
        "rv_comment":text,
        "ck":"oE4f",                          #这里的ck代表cookie，每个账号不一样
        "start":"0",
        "submit_btn":"加上去",
        # "captcha-solution":"damage",
        # "captcha-id": "WlrpdoeT5LS6YLO06Kfy9Ot3:en"
        # 后面两个是验证码
    }
    data = urllib.urlencode(values)
    # 创建请求的request
    request = urllib2.Request(url, data)
    # 此处的open方法同urllib2的urlopen方法，也可以传入request
    response = opener.open(request)
    # 打印获取的网页 (check the inject is success or not)
    # print response.read()
    try:
        soup = bs(response.read(), 'html.parser')
        print soup.title.string
    except StandardError:
        print 'something error'


if __name__ == '__main__':
    while True:
        # read the tiezi_id from files
        arr = []
        f = open('tiezi.txt')
        num = f.readlines()                 # 逐行读取文件，并生成数组
        for item in num:
            item = item.strip('\n')         # 去掉换行符
            print item                      # 后面跟 ',' 将忽略换行符
            arr.append(item)
        f.close()

        # inject & delete Loop
        for item in arr:
            # inject comment
            print '[inject comment]'
            injectComment(tiezi_id=item)
            time.sleep(60*2)

            # delete comment
            print '[delete comment]'
            deleteComment(tiezi_id=item)
            time.sleep(60*3)
        
        print '[wait for the next loop]'    
        time.sleep(60)





