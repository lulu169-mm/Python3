import requests
import re

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
# print(res.text)

# https://q8.itc.cn/q_70,c_zoom,h_1200,g_face/images01/20241010/f5424fd159e04cc5931de30656aaf966.png
# https://q6.itc.cn/q_70,c_zoom,h_1200,g_face/images01/20241010/39714dda73a449ebb0030ab5d3f37c98.png
# https://q6.itc.cn/q_70,c_zoom,h_1200,g_face/images01/20241010/5783030352024cc2acb545b48836f1e7.png
# https://q3.itc.cn/q_70,c_zoom,h_1200,g_face/images01/20241010/0314873f5b9e4a1585ce39a05f3a17ea.png
# https://q7.itc.cn/q_70,c_zoom,h_1200,g_face/images01/20241010/30b05926405e4459b08cd4efae804c3a.png

# TODO:使用正则提取所有图片链接,注意观察几张图片的规律
img_url = re.findall(r'//q[0-9].itc.cn/q_70,c_zoom,h_1200,g_face/images01/20241010/.*?.png', res.text)
# TODO:使用集合去重(唯一性)
end_urls = set(img_url)

# TODO:遍历所有图片链接并下载
for count, url in enumerate(end_urls, start=1):
    end_url = 'https:' + url
    print(f"下载图片: {end_url}")

    # TODO:下载
    res = requests.get(end_url, headers=headers)
    # TODO:这儿图片名字提供一个思路,使用bs4的get_text()方法获取所有文本,提取出来是一个列表,而且
    # TODO:是带有 \n\n\n\n 换行符这些的,就是说列表只有一个元素,那么需要指定位置切割字符串,去掉不需要的脏数据
    # TODO:然后在使用for循环遍历列表,把列表元素作为文件名
    with open(f'张纪中-{count}.png', 'wb') as f:
        f.write(res.content)
print("所有图片下载完成！")
