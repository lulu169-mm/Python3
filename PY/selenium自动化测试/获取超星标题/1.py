import requests
from bs4 import BeautifulSoup

url='http://www.chaoxing.com'
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}
res=requests.get(url,headers=headers)
# print(res.text)
#获取标题
print(res.text.split('<title>')[1].split('</title>')[0])

#找到ul标签中的所有文本即导航栏
soup=BeautifulSoup(res.text,'html.parser')
print(soup.find('ul').text)




