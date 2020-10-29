# -*- coding: UTF-8 -*-
# @Project -> File   ：ursky -> app_urls
# @IDE    ：PyCharm
# @Author ：YX
# @Date   ：2020/6/2 10:55

from django.urls import path
from . import views


urlpatterns = [
    #  /blog/
    path('', views.app, name='app_list'),
    #  /blog/[int]
    path('<int:app_id>', views.app, name='app'),
]