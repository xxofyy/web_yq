# -*- coding: UTF-8 -*-
# @Project -> File   ：website -> view
# @IDE    ：PyCharm
# @Author ：YX
# @Date   ：2020/6/7 12:26

from django.shortcuts import render

def lost(request):
    return render(request,'lost.html')