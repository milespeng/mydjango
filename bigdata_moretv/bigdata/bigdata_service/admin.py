# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import Service


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'cwd', 'user', 'cmd', 'port', 'host', 'logpath')
    list_filter = ('user', 'host')
    search_fields = ('name', 'user')
    fieldsets = ((None, {'fields': ('name', ('cwd', 'user'), ('cmd', 'port', 'host'), 'logpath',)}),)


admin.site.register(Service, ServiceAdmin)
