from django.db import models


# Create your models here.
class Manager(models.Model):
    mname = models.CharField('店长姓名', max_length=30)
    mgender = models.BooleanField('性别', null=True)
    mpnum = models.CharField('手机号码', max_length=11)
    mpasswd = models.CharField('密码', max_length=256)
    midnum = models.CharField('身份证号码', max_length=18)
    memail = models.CharField('邮箱', max_length=20)
    misapacity = models.BooleanField('是否活跃', default=1)
    mcreatedtime = models.DateTimeField('创建时间', auto_now_add=True)
    mjoinfunds = models.DecimalField('加盟资金', max_digits=9, decimal_places=2, default=0.0)
    mlitime = models.DateTimeField('加盟过期时间', default='2025-1-1 0:0:0')

    def __str__(self):
        return f'{self.mname}'


class Hotel(models.Model):
    hname = models.CharField('酒店名称', max_length=50)
    hphum = models.CharField('酒店电话', max_length=11, default='0000')
    hlocation = models.CharField('酒店地址', max_length=128, null=True)
    hmanager = models.ForeignKey(Manager, on_delete=models.CASCADE)
