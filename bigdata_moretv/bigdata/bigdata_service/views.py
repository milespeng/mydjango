# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

from .models import Service
from .forms import ServiceForm


# Create your views here.
def index(request):
    services = Service.objects.all()

    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            service = Service()
            service.name = cleaned_data['name']
            service.cwd = cleaned_data['cwd']
            service.user = cleaned_data['user']
            service.cmd = cleaned_data['cmd']
            service.port = cleaned_data['port']
            service.host = cleaned_data['host']
            service.logpath = cleaned_data['logpath']
            service.create_user = cleaned_data['create_user']
            service.zabbix_item = cleaned_data['zabbix_item']

            service.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = ServiceForm()

    context = {'services': services, 'form': form, }
    return render(request, 'index.html', context=context)
