from django.db import models

from search.models import Hotel


# Create your models here.
class Room(models.Model):
    isNull = models.BooleanField('是否入住', default=0)
    rtype = models.CharField('房型', max_length=100, default='标准间')
    rprice = models.DecimalField('价格', max_digits="7", decimal_places=2)
    rpeople = models.SmallIntegerField('入住人数', default=1)
    rimage = models.ImageField('房间图片', upload_to='roomImage', default='')
    # 外键链接
    rhotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
