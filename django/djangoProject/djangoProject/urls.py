# url和函数的对应关系，常常操作
"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app01 import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('index/',views.index),
    path('user/list',views.user_list),
    path('user/add',views.user_add),
    path('tpl/',views.tpl),

    path('news/',views.news),
    #用户登录
    path('login/',views.login),


    #案例：用户管理
    path('info/list/',views.info_list),
    # 用户信息添加
    path('info/add/',views.info_add),
    # 用户信息删除
    path('info/delete/',views.info_delete),
]
