import requests
from bs4 import BeautifulSoup as bp

# TODO:方法一
page = int(input("请输入想要爬取的章节数："))
for page in range(1, page + 1):
    # TODO:将章节数与url进行拼接
    url = f'https://www.shicimingju.com/book/shuihuzhuan/{page}.html'
    # TODO:放入请求头
    headers = {
        'authority': 'www.shicimingju.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'sec-ch-ua': '";Not A Brand";v="99", "Chromium";v="94"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 SE 2.X MetaSr 1.0',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://www.shicimingju.com/book/shuihuzhuan.html',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': 'Hm_lvt_649f268280b553df1f778477ee743752=1728461954; HMACCOUNT=34961B75D03086BC; Hm_lpvt_649f268280b553df1f778477ee743752=1728462095',
    }
    # print(url) # TODO:打印看看是否拼接成功
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'  # TODO:这里以防乱码，设置编码
    # print(response.text) # TODO:打印看看能否正常获取响应

    soup = bp(response.text, 'html.parser')
    # TODO:获取标题 <h1 class="bt">楔子 张天师祈禳瘟疫 洪太尉误走妖魔</h1>
    title = soup.find('h1').text
    print(title)
    # TODO:获取正文<div class="text p_pad">
    content = soup.find('div', class_='text p_pad').text
    print(content)
    with open(f'水浒传.txt', 'a', encoding='utf-8') as f:
        f.write('\n' + title + '\n' + content + '\n')

# TODO:方法二(需要驱动)
# from selenium import webdriver as wd
# from lxml import etree
#
# page = int(input("请输入想要爬取的章节数："))
# for page in range(1, page + 1):
#     url = f'https://www.shicimingju.com/book/shuihuzhuan/{page}.html'
#
#     # TODO:启动浏览器
#     driver = wd.Edge()
#     driver.get(url)
#
#     # TODO:获取响应
#     data = driver.page_source
#     html = etree.HTML(data)
#
#     # TODO:提取内容
#     content = html.xpath("//div[@class='text p_pad']/text()")
#     for i in content:
#         print(i)
#
#     # TODO:关闭浏览器
#     driver.quit()
