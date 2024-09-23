from django.shortcuts import render, redirect
from app01 import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django import forms
from app01.untils.pagination import Pagination


# Create your views here.
def depart_list(request):
    """部门列表"""
    # 获取部门列表数据
    # [对象,对象,对象] --->列表
    queryset = models.Department.objects.all()

    # page_object = Pagination(request, queryset, page_size=5)
    # context = {
    #     'queryset': page_object.page_queryset,
    #     'page_string': page_object.html(),
    # }

    return render(request, 'depart_list.html', {'queryset': queryset})  # 原版

    # return render(request, 'depart_list.html', context) #考虑到部门可能只需要1页即可，所以使用不使用分页


def depart_add(request):
    """添加部门"""
    if request.method == 'GET':
        return render(request, 'depart_add.html')
    # 获取用户提交的数据
    title = request.POST.get('title')
    # 保存到数据库
    models.Department.objects.create(title=title)
    # 跳转到部门列表页面
    return redirect('/department/list/')


def depart_delete(request):
    """删除部门"""
    # 获取用户提交的要删除的部门ID
    nid = request.GET.get('nid')
    # 删除
    models.Department.objects.filter(id=nid).delete()
    # 跳转
    return redirect('/department/list/')


def depart_edit(request, nid):
    """编辑部门"""
    # 获取要编辑的部门对象
    if request.method == 'GET':
        row_object = models.Department.objects.filter(id=nid).first()
        print(row_object.id, row_object.title)
        return render(request, 'depart_edit.html', {'row_object': row_object})
    models.Department.objects.filter(id=nid).update(title=request.POST.get('title'))
    return redirect('/department/list/')


def user_list(request):
    """用户管理"""
    # 获取用户列表数据
    queryset = models.UserInfo.objects.all()

    page_object = Pagination(request, queryset, page_size=10)
    context = {
        'queryset': page_object.page_queryset,
        'page_string': page_object.html(),
    }
    # for obj in queryset:
    # 表关联，通过department_id获取tirle——>obj.department.title
    # print(obj.id, obj.name, obj.password, obj.age, obj.salary, obj.create_time.strftime("%Y-%m-%d"), obj.get_gender_display(), obj.department.title)
    # return render(request, 'user_list.html', {'queryset': queryset}) #原版

    return render(request, 'user_list.html', context)  # 使用封装分页后的版本


# def user_add(request):
#     """添加用户"""
#     if request.method == 'GET':
#         context = {
#             'gender_choices': models.UserInfo.gender_choices,
#             'depart_list': models.Department.objects.all()
#         }
#         return render(request, 'user_add.html', context)
#
#     # 获取用户提交的数据
#     user = request.POST.get('user')
#     password = request.POST.get('password')
#     age = request.POST.get('age')
#     salary = request.POST.get('salary')
#     ctime = request.POST.get('ctime')
#     gender_id = request.POST.get('gd')
#     depart_id = request.POST.get('dp')
#
#     # 保存到数据库
#     models.UserInfo.objects.create(name=user, password=password, age=age, salary=salary, create_time=ctime,
#                                    gender=gender_id, department_id=depart_id)
#
#     # 跳转到用户列表页面
#     return redirect('/user/list/')


# ————————————————————————————————————ModelForm版本——————————————————————————————————————


class UserModelForm(forms.ModelForm):
    class Meta:
        model = models.UserInfo
        fields = ['name', 'password', 'age', 'salary', 'create_time', 'gender', 'department']

        # 初学者添加control
        # widgets = {
        #     "name": forms.TextInput(attrs={"class": "form-control"}),
        #     "password": forms.PasswordInput(attrs={"class": "form-control"}),
        #     "age": forms.TextInput(attrs={"class": "form-control"}),
        #     "salary": forms.TextInput(attrs={"class": "form-control"}),
        #     "create_time": forms.TextInput(attrs={"class": "form-control"}),
        #     "gender": forms.Select(attrs={"class": "form-control"}),
        #     "department": forms.Select(attrs={"class": "form-control"}),
        # }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 统一给字段添加样式 class="form-control""
        for name, field in self.fields.items():
            # 排除 password 字段
            # if name == 'password':
            #     continue

            # 添加样式
            field.widget.attrs = {'class': 'form-control', 'placeholder': field.label}


def user_model_form_add(request):
    """添加用户（ModelForm版本）"""
    if request.method == 'GET':
        form = UserModelForm()
        return render(request, 'user_model_form_add.html', {'form': form})
    # 用户post提交数据，数据校验。
    form = UserModelForm(data=request.POST)
    if form.is_valid():
        # {'name': '李敏', 'password': '111', 'age': 21, 'salary': Decimal('0'), 'create_time': datetime.datetime(2021, 11, 23, 0, 0, tzinfo=zoneinfo.ZoneInfo(key='UTC')), 'gender': 2, 'department': <Department: 运营部>}
        # print(form.cleaned_data)
        form.save()
        return redirect('/user/list')
    # 如果校验失败
    return render(request, 'user_model_form_add.html', {'form': form})


def user_edit(request, nid):
    """编辑用户"""
    row_object = models.UserInfo.objects.filter(id=nid).first()

    if request.method == 'GET':
        # 根据id取数据获取要编辑的那一行数据
        row_object = models.UserInfo.objects.filter(id=nid).first()
        form = UserModelForm(instance=row_object)
        return render(request, 'user_edit.html', {'form': form})

    form = UserModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/user/list/')
    return render(request, 'user_edit.html', {'form': form})


def user_delete(request, nid):
    """删除用户"""
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect('/user/list/')


def prettynum_list(request):
    """靓号列表"""
    data_dict = {}
    search_data = request.GET.get('q', '')
    if search_data:
        data_dict['mobile__contains'] = search_data

    queryset = models.PrettyNum.objects.filter(**data_dict).all()

    page_object = Pagination(request, queryset)

    context = {
        "search_data": search_data,
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 页码
    }

    return render(request, 'prettynum_list.html', context)


class PrettyModelForm(forms.ModelForm):
    # TODO:验证方式一
    mobile = forms.CharField(
        label='手机号',
        validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机号格式错误')]
    )

    class Meta:
        model = models.PrettyNum
        # fileds=['mobile', 'level', 'status'] 写哪些出现哪些
        # fields = '__all__'
        # exclude=['level'] 排除

        fields = ['mobile', 'price', 'level', 'status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {'class': 'form-control', 'placeholder': field.label}

    # TODO:验证方式二
    # def clean_mobile(self):
    #     txt_mobile = self.cleaned_data['mobile']
    #     if len(txt_mobile) != 11:
    #         # 验证失败，抛出异常
    #         raise ValidationError('手机号格式错误')
    #
    #     # 验证通过，返回值
    #     return txt_mobile


def prettynum_add(request):
    """添加靓号"""
    if request.method == 'GET':
        form = PrettyModelForm()
        return render(request, 'prettynum_add.html', {'form': form})
    # 用户post提交数据，数据校验。
    form = PrettyModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/prettynum/list/')
    # 如果校验失败
    return render(request, 'prettynum_add.html', {'form': form})


class PrettyEditModelForm(forms.ModelForm):
    # mobile = forms.CharField(disabled=True, label='手机号')  # 不可编辑手机号

    class Meta:
        model = models.PrettyNum
        fields = ['mobile', 'price', 'level', 'status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {'class': 'form-control', 'placeholder': field.label}


def prettynum_edit(request, nid):
    """编辑靓号"""
    row_object = models.Department.objects.filter(id=nid).first()
    if request.method == 'GET':
        # 根据id取数据获取要编辑的那一行数据
        row_object = models.PrettyNum.objects.filter(id=nid).first()
        form = PrettyEditModelForm(instance=row_object)
        return render(request, 'prettynum_edit.html', {'form': form})

    form = PrettyEditModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/prettynum/list/')
    return render(request, 'prettynum_edit.html', {'form': form})


# TODO：编辑靓号时校验号码是否存在，（需要将211行，不可编辑手机号 注释掉才可使用）
def clean_mobile(self):
    # 如果是编辑，排除自己
    # print(self.instance.pk)
    txt_mobile = self.cleaned_data['mobile']
    exists = models.PrettyNum.objects.exclude(id=self.instance.pk).filter(mobile=txt_mobile).exists()
    if exists:
        raise ValidationError('手机号已存在')
    return txt_mobile


def prettynum_delete(request, nid):
    """删除靓号"""
    models.PrettyNum.objects.filter(id=nid).delete()
    return redirect('/prettynum/list/')

