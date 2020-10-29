from django.shortcuts import render,redirect
from django.contrib.contenttypes.models import ContentType
from .models import Comment
from django.urls import reverse

def update_comment(request):
    text = request.POST.get('text','').strip()
    # 检查数据
    if text =='':
        return  render(request,'lost.html',{'message':'评论内容不能为空'})
    try:
        content_type = request.POST.get('content_type','')
        object_id = int(request.POST.get('object_id',''))
        model_class = ContentType.objects.get(model=content_type).model_class()
        model_obj = model_class.objects.get(pk=object_id)
    except:
        return render(request,'lost.html',{'message':'评论对象不存在'})
    # 检查通过
    comment = Comment()
    comment.author = request.user
    comment.text = text
    comment.content_object =model_obj
    comment.save()

    referer = request.META.get('HTTP_REFERER', reverse('home'))
    return redirect(referer)
