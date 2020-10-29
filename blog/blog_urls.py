# -*- coding: UTF-8 -*-
# @Project -> File   ：ursky -> blog_urls
# @IDE    ：PyCharm
# @Author ：YX
# @Date   ：2020/6/1 21:04

from django.urls import path
from . import views


urlpatterns = [
    #  /blog/
    path('', views.blog_list, name='blog_list'),
    #  /demos/[int]
    path('<int:blog_pk>', views.blog_detail, name='blog_detail'),
    path('type/<int:blog_type_pk>', views.blog_with_type, name='blog_with_type'),
]