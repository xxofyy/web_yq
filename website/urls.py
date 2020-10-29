"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from home import views
from .view import lost

urlpatterns = [
    path('rt/', admin.site.urls),
    path('ckeditor',include('ckeditor_uploader.urls')),
    path('',views.welcome,name='welcome'),
    path('home/',views.home,name='home'),
    path('lost/',lost,name='lost'), # self lost
    path('blog/',include('blog.blog_urls')),# blog网页
    path('app/', include('apps.app_urls')), # qpp 网页
    path('comment/', include('comment.urls')),
    path('login/', views.login,name='login'),
    path('logout/', views.logout,name='logout'),
    path('register/', views.register,name='register'),
]
urlpatterns += static('/media/',document_root=settings.MEDIA_ROOT)