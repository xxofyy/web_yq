from django.shortcuts import render, redirect
from apps.models import AppName
from django.contrib import auth
from django.contrib.auth.models import User,Group,ContentType
from django.urls import reverse
from home.models import LoginForm,RegForm



def welcome(request):
    return render(request, 'welcome.html')


def home(request):
    context = {}
    context['apps'] = AppName.objects.all()
    return render(request,'yqlz.html',context)


def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = login_form.cleaned_data['user']
            auth.login(request,user)
            return redirect(request.GET.get('from',reverse('home')))
    else:
        login_form = LoginForm()
    context = {}
    context['login_form']=login_form
    return render(request,'Login.html',context)


def register(request):
    if request.method=='POST':
        reg_form = RegForm(request.POST)
        if reg_form.is_valid():
            username=reg_form.cleaned_data['username']
            email = reg_form.cleaned_data['email']
            password = reg_form.cleaned_data['password']
            xing = reg_form.cleaned_data['xing']
            ming = reg_form.cleaned_data['ming']
            # 创建用户
            # 添加到组
            user = User.objects.create_user(username=username,email=email,password=password,first_name=xing,last_name=ming)
            group = Group.objects.filter(name='游客').first()
            user.groups.add(group)
            user.save()
            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
            return redirect('/')
    else:
        reg_form = RegForm()

    context = {}
    context['reg_form'] = reg_form
    return render(request,'Register.html',context)

def logout(request):
    auth.logout(request)
    return redirect(request.GET.get('from',reverse('home')))
