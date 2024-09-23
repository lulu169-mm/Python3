from django.shortcuts import render, HttpResponse, redirect

from app01.models import UserInfo


# Create your views here.
def index(request):
    return HttpResponse("欢迎使用！")


def user_list(request):
    return render(request, 'user_list.html')


def user_add(request):
    return HttpResponse("添加用户")


def tpl(request):
    name = '孙华'
    roles = ['管理员', 'CEO', '保安']
    user_info = {"name": "孙华", "salary": 100000, "role": "CEO"}

    data_list = [
        {"name": "张三", "salary": 10000, "role": "员工"},
        {"name": "李四", "salary": 20000, "role": "经理"},
        {"name": "王五", "salary": 30000, "role": "总监"},
    ]
    return render(request, 'tpl.html', {"n1": name, "n2": roles, "n3": user_info, "n4": data_list})


def news(req):
    # 定义一些新闻（字典或列表） 或 去数据库取 网络请求去新闻
    import requests
    url = 'https://news.cctv.com/2019/07/gaiban/cmsdatainterface/page/china_1.jsonp?cb=china'
    res = requests.get(url)
    data_list = res.content.decode('utf-8')
    print(data_list)

    return render(req, 'news.html', {"news_list": data_list})


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')

        # print(request.POST)
    username = request.POST.get('username')
    password = request.POST.get('password')

    # 验证用户名和密码
    if username == 'admin' and password == '123':
        # return HttpResponse("登录成功")
        # 重定向百度
        return redirect('https://www.baidu.com/')
    # return HttpResponse("用户名或密码错误")
    return render(request, 'login.html', {"error_msg": "用户名或密码错误"})


def info_list(request):
    # 获取数据库中的所有用户信息
    data_list = UserInfo.objects.all()
    print(data_list)
    return render(request, 'info_list.html', {"data_list": data_list})


def info_add(request):
    if request.method == "GET":
        return render(request, 'info_add.html')

    # 获取用户提交数据
    name = request.POST.get('username')
    password = request.POST.get('password')
    age = request.POST.get('age')

    # 创建用户信息
    UserInfo.objects.create(name=name, password=password, age=age)

    # 重定向到用户列表页面
    return redirect('/info/list/')


def info_delete(request):
    # 获取要删除的用户ID
    nid = request.GET.get('nid')
    UserInfo.objects.filter(id=nid).delete()
    return redirect('/info/list/')
