import requests
import re
from lxml import etree
from bs4 import BeautifulSoup


# 请求页面内容
headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'sec-ch-ua': '";Not A Brand";v="99", "Chromium";v="94"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 SE 2.X MetaSr 1.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://www.sohu.com/',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cookie': 'IPLOC=CN; SUV=241010141919P4WV; cityIpLocation=111.55.145.64; reqtype=pc; gidinf=x099980109ee199821fbce0140002b75f45afe2835f2; _dfp=s68j8Ud8GOW0/csPXMu+b4+2vkPuvOt/qIYBuWjX2+U=; clt=1728541160; cld=20241010141920; arialoadData=false; beans_new_turn=%7B%22www.sohu.com%22%3A23%7D; t=1728541336391; 15853=2',
}

res = requests.get(
    'https://www.sohu.com/picture/815143309?spm=smpc.home.yule-pics.1.1728541255950wYU2Yfh_1467&_f=index_yulefocus_0_0&scm=thor.543_14-200000.0.10006.',
    headers=headers)
res.encoding = 'utf-8'

# 解析HTML内容为纯文本
parser = etree.HTMLParser()
soup = BeautifulSoup(res.text, 'html.parser')
# 提取页面的纯文本
text = soup.get_text()
# 打印结果
print(text)

