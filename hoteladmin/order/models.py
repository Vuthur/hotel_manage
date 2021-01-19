from django.db import models


# Create your models here.
class Room(models.Model):
    isNull = models.BooleanField('是否入住', default=0)
    rtype = models.CharField('房型', max_length=100, default='标准间')
    rprice = models.DecimalField('价格', max_digits="7", decimal_places=2)
    rpeople = models.SmallIntegerField('入住人数', default=1)
    # 外键链接
