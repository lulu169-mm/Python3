"""
URL configuration for usermanage project.

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

    # 部门管理
    path('department/list/', views.depart_list),
    path('department/add/', views.depart_add),
    path('department/delete/', views.depart_delete),
    path('department/<int:nid>/edit/', views.depart_edit),

    # 用户管理
    path('user/list/', views.user_list),
    # path('user/add/', views.user_add),
    path('user/model/form/add/', views.user_model_form_add),
    path('user/<int:nid>/edit/', views.user_edit),
    path('user/<int:nid>/delete/', views.user_delete),

    # 靓号管理
    path('prettynum/list/', views.prettynum_list),
    path('prettynum/add/', views.prettynum_add),
    path('prettynum/<int:nid>/edit/', views.prettynum_edit),
    path('prettynum/<int:nid>/delete/', views.prettynum_delete),
]

