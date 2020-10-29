from django.shortcuts import render
from .models import AppName
# Create your views here.

def app(request,app_id):
    try:
        context = {}
        if app_id == 12:
            context['app'] = AppName.objects.get(pk=app_id)
            return render(request,'app.html', context)
        else:
            context['app'] = AppName.objects.get(pk=app_id)
            return render(request, 'app.html', context)
    except:
        return render(request,'lost.html')