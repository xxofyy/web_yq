# -*- coding: UTF-8 -*-
# @Project -> File   ：website -> urls
# @IDE    ：PyCharm
# @Author ：YX
# @Date   ：2020/6/10 9:03

from django.urls import path
from . import views


urlpatterns = [
    #  /blog/
    path('update_comment', views.update_comment, name='update_comment'),

]