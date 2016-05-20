#coding=utf-8

#豆瓣电影 cookie
# import urllib2
# import urllib

# values = {'search_text':'狼人', 'cat':1002}
# url = "http://movie.douban.com/subject_search"
# data = urllib.urlencode(values)

# request = urllib2.Request(url, data)
# response = urllib2.urlopen(request)
# print response.read()



# Python读取文件
# f = open("taici.txt")             # 返回一个文件对象
# line = f.readline()               # 调用文件的 readline()方法
# while line:
#     print line,                   # 后面跟 ',' 将忽略换行符
#     line = f.readline()

# f.close()


f = open('taici.txt')
num = f.readlines()                 # 逐行读取文件，并生成数组
print num[3],                       # 后面跟 ',' 将忽略换行符
f.close()






