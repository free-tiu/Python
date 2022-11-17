from django.db import models


class Department(models.Model):
    """ 部门表 """
    title = models.CharField(max_length=32, verbose_name='标题')


class UserInfo(models.Model):
    """ 员工表 """
    name = models.CharField(max_length=32, verbose_name='姓名')
    password = models.CharField(max_length=32, verbose_name='密码')
    age = models.IntegerField(verbose_name='年龄')
    # Decimal：准确的小数值，m是是数字总个数（符号不算），最大值为65；d是小数点后长度，最大值为30
    account = models.DecimalField(verbose_name='账户余额', max_digits=10, decimal_places=2, default=0)
    create_time = models.DateTimeField(verbose_name='入职时间')

    # 外键约束 to="需要对应的表名", to_field="需要对应的字段"
    depart = models.ForeignKey(to="Department", to_field="id", null=True, blank=True, on_delete=models.SET_NULL)

    # 性别元组
    gender_choices = [
        (1, "男"),
        (2, "女"),
    ]
    gender = models.SmallIntegerField(verbose_name='性别', choices=gender_choices)



