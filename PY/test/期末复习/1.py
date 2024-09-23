import urllib.request  # 导入 urllib.request 模块
from fake_useragent import UserAgent  # 导入 UserAgent 类

def getUrl(url, key, value, index):
    import urllib.parse  # 导入 urllib.parse 模块
    d = {
        key: value  # 创建包含 key-value 对的字典
    }
    #TODO:urlencode关键字需要记住
    pd = urllib.parse.urlencode(d)  # 将字典编码成 URL 查询参数字符串
    url = url + index + "/?" + pd  # 构建完整的 URL
    ua = UserAgent()  # 创建 UserAgent 对象
    header = {
        'User-Agent': ua.random  # 设置请求头中的 User-Agent 字段为随机值
    }


    request = urllib.request.Request(url, headers=header)  # 创建请求对象

    # TODO:urlopen关键字需要记住
    res=urllib.request.urlopen(request)  # 发送请求并获取响应对象
    html = res.read().decode("utf-8")  # 读取响应内容并解码为 UTF-8 编码的字符串
    print(html)  # 打印响应内容

if __name__ == "__main__":
    getUrl("https://cd.58.com/ershoufang/p", "q", "绿地", "1")  # 调用 getUrl 函数，并传递参数
