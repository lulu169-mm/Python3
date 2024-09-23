from lxml import etree
from selenium import webdriver as wd
import time

keyword=input('请输入要搜索的图片：')
url=f'https://image.baidu.com/search/index?tn=baiduimage&fm=result&ie=utf-8&word={keyword}'
driver=wd.Edge()
driver.get(url)
time.sleep(1)

data=driver.page_source
html=etree.HTML(data)

# 获取图片链接
img_urls=html.xpath('//*[@id="imgid"]/div[1]/ul/li[*]/div/div[2]/a/img/@src')
print(img_urls)
