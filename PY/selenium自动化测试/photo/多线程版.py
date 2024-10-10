import requests
import re
from tqdm import tqdm
from colorama import Fore
from concurrent.futures import ThreadPoolExecutor

# 网站的基础URL
url = 'https://www.scit.cn'

# 页面的URL
urls = url + '/zszx_wskx.htm'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}
# 发起请求获取页面内容
res = requests.get(urls, headers=headers)
# 获取服务器返回的页面内容
res_html = res.text

# 正则表达式匹配图片文件路径
imgs_pattern = r'/Imgfile/themeimg/[a-z0-9_]+\.jpg'
# findall函数会返回一个列表，包含所有匹配正则表达式的字符串
img_urls = re.findall(imgs_pattern, res_html)

# 获取奇数位的图片URL
odd_img_urls = [img_url for i, img_url in enumerate(img_urls) if i % 2 != 0]

def download_image(img_url, index):
    # 拼接
    full_url = url + img_url
    # 再次发送请求，下载图片
    img_res = requests.get(full_url)
    # 打开一个文件，以二进制写入模式
    # 文件名为'scit_'加上图片编号，扩展名为'.jpg'
    with open(f'scit_{index + 1}.jpg', mode='wb') as f:
        f.write(img_res.content)

# 使用ThreadPoolExecutor实现多线程下载
with ThreadPoolExecutor(max_workers=30) as executor:
    list(tqdm(executor.map(lambda p: download_image(p[1], p[0]), enumerate(odd_img_urls)), total=len(odd_img_urls), desc=Fore.CYAN + '正在下载图片'))

print("下载完成！")
