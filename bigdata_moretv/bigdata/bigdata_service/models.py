# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from .config import USER_ITEM

# Create your models here.
class Service(models.Model):
    #USER_ITEM = [(1, "moretv"), (2, 'hdfs'), (3, 'yarn'), (4, 'storm'), (5, 'spark')]
    name = models.CharField(max_length=128, verbose_name='服务名称')
    cwd = models.CharField(max_length=128, verbose_name='工作路径')
    user = models.IntegerField(choices=USER_ITEM, verbose_name='工作用户')
    cmd = models.CharField(max_length=128, verbose_name='启动命名')
    port = models.CharField(max_length=128, verbose_name="服务端口")
    host = models.CharField(max_length=128, verbose_name="部署服务器")
    logpath = models.CharField(max_length=128, verbose_name="日志路径")
    create_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="创建时间")
    create_user = models.CharField(max_length=20, verbose_name='登记人员')
    zabbix_item = models.CharField(max_length=128, verbose_name='zabbix报警')

    def __unicode__(self):
        return '<Service: {}>'.format(self.name)
