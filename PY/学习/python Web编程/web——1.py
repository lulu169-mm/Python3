# 使用urlparse方法进行url解析
# from urllib.parse import urlparse
# result=urlparse('http://www.baidu.com/index.html;user?id=520#main')
# print(result) #输出结果为 ParseResult(scheme='http', netloc='www.baidu.com', path='/index1.html', params='user', query='id=520', fragment='main')
# print(type(result)) #输出结果为 <class 'urllib.parse.ParseResult'>
# print(result.netloc) #输出结果为 www.baidu.com
# print(result.path) #输出结果为 /index1.html
# print(result.params) #输出结果为 user
# print(result.query) #输出结果为 id=520
# print(result.fragment) #输出结果为 main
# print(result.username) #输出结果为 None
# print(result.password) #输出结果为 None
# print(result.hostname) #输出结果为 www.baidu.com
# print(result.port) #输出结果为 None
# print(result.geturl()) #输出结果为 http://www.baidu.com/index.html;user?id=520#main
# print(result.scheme) #输出结果为 http
# print(result[0]) #输出结果为 http

#分解url urlsplit和urlparse的区别
# from urllib.parse import urlparse, urlsplit
# url='http://www.baidu.com/index.html;user?id=520#main'
# result1=urlparse(url)
# result2=urlsplit(url)
# print(result1) #输出结果为 ParseResult(scheme='http', netloc='www.baidu.com', path='/index1.html', params='user', query='id=520', fragment='main')
# print(result2) #输出结果为 SplitResult(scheme='http', netloc='www.baidu.com', path='/index1.html', query='id=520', fragment='main')

import django
print(django.VERSION)