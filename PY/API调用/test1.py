import requests

url = "https://zj.v.api.aa1.cn/api/qqmusic/demo.php"

data ={
    "n": "输出音乐数量 默认为5 （不能大于30）",
    "tips": "提示",
    "count": "歌曲总数 type为1时 恒定为100条，建议使用瀑布流实现",
    "list": {
        "name": "歌曲名",
        "singer": "歌手名",
        "cover": "图片链接",
        "url": "下载前置页"
    },
    "code": "错误码",
    "msg": "描述"
}
res=requests.get(url,data)
print(res.content)



