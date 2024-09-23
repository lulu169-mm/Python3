from django.db import models


# 部门管理
class Department(models.Model):
    """部门表"""
    # id=models.AutoField(primary_key=True,verbose_name='部门ID')
    title = models.CharField(verbose_name='部门标题', max_length=32)

    # 重写__str__方法，返回部门标题,类似java的 toString()
    def __str__(self):
        return self.title


class UserInfo(models.Model):
    """员工表"""
    name = models.CharField(verbose_name='员工姓名', max_length=16)
    password = models.CharField(verbose_name='员工密码', max_length=64)
    age = models.IntegerField(verbose_name='员工年龄')  # 整形不用加长度
    salary = models.DecimalField(verbose_name='员工工资', max_digits=8, decimal_places=2, default=0)  # 8位整数，2位小数, 默认值为0
    # create_time = models.DateTimeField(verbose_name='创建时间')
    create_time = models.DateField(verbose_name='创建时间')

    # 无约束
    # depart_id=models.BigIntegerField(verbose_name='部门ID')

    # 1.有约束
    # -to 表示关联的表
    # -to_field 表示关联表中的字段
    # 2.django自动
    # -写的depart
    # -自动加_id
    # 3.部门表被删除
    # -级联删除 depart=models.ForeignKey(verbose_name='部门ID',to='Department',to_field='id',on_delete=models.CASCADE)
    # -置空 depart=models.ForeignKey(verbose_name='部门ID',to='Department',to_field='id',on_delete=models.SET_NULL,null=True)

    # 部门id加约束，生成数据列会自动加 depart_id （_id）
    department = models.ForeignKey(verbose_name='部门', to='Department', to_field='id',
                                   on_delete=models.CASCADE)  # 部门ID，外键，关联部门表的ID字段，级联删除

    # 在django中做的约束
    gender_choices = (
        (1, '男'),
        (2, '女'),
    )
    gender = models.SmallIntegerField(verbose_name='性别', choices=gender_choices)


from django.db import models


class PrettyNum(models.Model):
    """靓号表"""
    mobile = models.CharField(verbose_name='手机号', max_length=11)
    price = models.IntegerField(verbose_name='价格', default=0, null=True, blank=True)

    level_choices = (
        (1, '1级'),
        (2, '2级'),
        (3, '3级'),
        (4, '4级'),
    )
    level = models.SmallIntegerField(verbose_name='级别', choices=level_choices, default=1)

    status_choices = (
        (1, '未使用'),
        (2, '已使用'),
    )
    status = models.SmallIntegerField(verbose_name='状态', choices=status_choices, default=1)
