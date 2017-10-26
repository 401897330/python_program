from django.db import models

class BoxInfo(models.Model):
    request_time = models.DateTimeField(verbose_name="请求时间")
    ip = models.CharField(verbose_name="请求ip", max_length=32)
    sn_addr = models.CharField(verbose_name="盒子地址", max_length=64)
    channel = models.CharField(verbose_name="频道名", max_length=32)
    stream = models.CharField(verbose_name="请求码流", max_length=32)
    request_addr = models.CharField(verbose_name="请求节点", max_length=32)
    sn = models.CharField(verbose_name="盒子号", max_length=32)
    ht = models.BooleanField(verbose_name="是否启用超线程")
    status = models.CharField(verbose_name="请求状态码", max_length=12)
    down_time = models.CharField(verbose_name="本次下载时间", max_length=12)
    ts_num = models.CharField(verbose_name="ts号", max_length=32)
    netspeed = models.CharField(verbose_name="网速",max_length=12)


class UserInfo(models.Model):
    username = models.CharField(verbose_name="用户名", max_length=12)
    password = models.CharField(verbose_name="密码", max_length=64)
