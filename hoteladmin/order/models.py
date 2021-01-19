from django.db import models

from search.models import Hotel


# Create your models here.
class Room(models.Model):
    rtype = models.CharField('房型', max_length=100, default='标准间')
    rprice = models.DecimalField('价格', max_digits="7", decimal_places=2)
    rpeople = models.SmallIntegerField('入住人数', default=1)
    rimage = models.ImageField('房间图片', upload_to='roomImage', default='')
    # 外键链接
    rhotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)


class RoomStatus(models.Model):
    stime = models.DateField('预定时间')
    rnull = models.BooleanField('是否为空', default=1)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
