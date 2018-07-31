# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse
import json

# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        list01 = request.POST.get('list01')
        print(name)
        print(age)
        print(list01)

        # list02 = {'status':0,
        #           'company':[{'name':'百度','age':28},
        #                      {'name':'腾讯','age':30}
        #                      ]
        #           }

        list02 = {'status': 1,
                  'error':'用户名已被注册'
                  }
        # list02是一个列表，需要转换成字符串才能传回前端
        list02_str = json.dumps(list02)

        return HttpResponse(list02_str)
    return render(request, 'index.html')






