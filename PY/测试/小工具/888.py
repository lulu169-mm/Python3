# import requests
# from bs4 import BeautifulSoup as bp
#
# page = int(input("请输入您要获取的章节数:"))
# for pages in range(1, page + 1):
#     # f-string, .format
#     base_url = "https://www.shicimingju.com/book/shuihuzhuan/{}.html".format(pages)
#     # print(base_url)
#     header = {
#         'authority': 'www.shicimingju.com',
#         'pragma': 'no-cache',
#         'cache-control': 'no-cache',
#         'sec-ch-ua': '";Not A Brand";v="99", "Chromium";v="94"',
#         'sec-ch-ua-mobile': '?0',
#         'sec-ch-ua-platform': '"Windows"',
#         'upgrade-insecure-requests': '1',
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 SE 2.X MetaSr 1.0',
#         'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#         'sec-fetch-site': 'same-origin',
#         'sec-fetch-mode': 'navigate',
#         'sec-fetch-user': '?1',
#         'sec-fetch-dest': 'document',
#         'referer': 'https://www.shicimingju.com/book/shuihuzhuan.html',
#         'accept-language': 'zh-CN,zh;q=0.9',
#         'cookie': 'Hm_lvt_649f268280b553df1f778477ee743752=1728461954; HMACCOUNT=34961B75D03086BC; Hm_lpvt_649f268280b553df1f778477ee743752=1728462095',
#     }
#     res = requests.get(base_url, headers=header)
#     res.encoding = 'utf-8'
#     html = res.text
#     # print(res.text)
#     soup = bp(html, 'lxml')
#     # print(soup)
#
#     title = soup.find('h1', ).string
#     print(title)
#     content = soup.find('div', class_='text p_pad').text
#
#     with open('三国演绎.txt', 'a', encoding='utf-8') as f:
#          f.write('\n'+title + '\n' + content + '\n')

from selenium import webdriver as wd
from lxml import etree

page = int(input("请输入想要爬取的章节数："))
for page in range(1, page + 1):
    url = f'https://www.shicimingju.com/book/shuihuzhuan/{page}.html'
    driver = wd.Edge()
    driver.get(url)
    data = driver.page_source
    html = etree.HTML(data)

    title = html.xpath("//h1[@class='bt']/text()")
    # print(title)

    content = html.xpath("//div[@class='text p_pad']/text()")
    for contents in content:
        print(contents)
