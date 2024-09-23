import requests

url="http://ese3a7b7c6d3pk-pub.pub.qiqiuyun.net/37763/9c9b5394341948a385e2baaf7ea2f2f7/lsRti7mOeIeT7BhD-merged-shd_seg_0_ehls_fc9c82?schoolId=37763&fileGlobalId=9c9b5394341948a385e2baaf7ea2f2f7&userId=15248&userName=%E5%9B%9E%E5%BF%86%E6%8B%BC%E5%A5%BD%E4%B8%A2%E4%BA%86"
response=requests.get(url)
print(response.content)
with open("1.mp4","wb") as f:
        f.write(response.content)