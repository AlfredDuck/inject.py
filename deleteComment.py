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



# 删除评论

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
    values = {"cid": cid,
              "ck":"aSyc",                          #这里的ck代表cookie，每个账号不一样
              # "captcha-solution":"sweet",
              # "captcha-id": "JMsHm70CaUbKZta1uChuKIVm:en"
              # 后面两个是验证码
              }
    data = urllib.urlencode(values)
    url = 'https://www.douban.com/j/group/topic/' + tiezi_id + '/remove_comment'

    #创建请求的request
    request = urllib2.Request(url, data)
    #此处的open方法同urllib2的urlopen方法，也可以传入request
    response = opener.open(request)
    #打印获取的网页
    # print response.read()



def deleteComment (tiezi_id):

    url  = 'https://www.douban.com/group/topic/' + tiezi_id + '/'
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
        result = comments.find(href='https://www.douban.com/people/alfredduck/')
        # print result
        ding = result.parent.parent.find(class_='lnk-reply')
        text = ding['href']
    except StandardError:
        print '未找到需要删除的评论'
    else:
        # print result.parent.parent
        ding = result.parent.parent.find(class_='lnk-reply')
        print ding['href']

        # 正则提取出评论id
        text = ding['href']
        pattern = re.compile('cid=(.*)#last')
        result = pattern.search(text).group(1)
        print '要删除的评论id：', result

        # step 2
        postDeleteRequest(cid=result, tiezi_id=tiezi_id)




if __name__ == '__main__':

    # 读取要删除评论的帖子id
    arr = []
    f = open('tiezi.txt')
    num = f.readlines()                 # 逐行读取文件，并生成数组
    for item in num:
        item=item.strip('\n')           # 去掉换行符
        print item                      # 后面跟 ',' 将忽略换行符
        arr.append(item)
    f.close()
    print '帖子id:'
    print arr

    # 定时器（循环 + 间隔）
    while True:
        for item in arr:
            # 删除评论
            deleteComment(tiezi_id=item)
            time.sleep(30)

        time.sleep(60*7)                       # 这里的sleep参数是 n 秒









