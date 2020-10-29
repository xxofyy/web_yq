from django.shortcuts import render, get_object_or_404
from .models import Blog, BlogType,ReadNum
from django.contrib.contenttypes.models import ContentType
from comment.models import Comment
from comment.forms import CommentForm
from django.core.paginator import Paginator


def blog_list(request):
    blogs_all_list = Blog.objects.filter(is_deleted=False)
    paginator = Paginator(blogs_all_list,6)
    page_num = request.GET.get('page', 1)  # 获取页面参数
    page_of_blogs = paginator.get_page(page_num)
    current_page_num = page_of_blogs.number  #获取当前页码
    # 获取当前页的前后页码范围
    page_range = list(range(max(current_page_num-2,1),current_page_num)) + \
                 list(range(current_page_num,min(current_page_num+2,paginator.num_pages)+1))
    # 省略
    if page_range[0]-1>=2:
        page_range.insert(0,'...')
    if paginator.num_pages-page_range[-1]>=2:
        page_range.append('...')

    # 首页尾页
    if page_range[0] != 1:
        page_range.insert(0,1)

    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)


    context = {}
    context['page_of_blogs'] = page_of_blogs
    context['page_range'] = page_range
    context['blog_types'] = BlogType.objects.all()
    return render(request,'blog_list.html', context)

def blog_detail(request,blog_pk):
    blog = get_object_or_404(Blog, pk = blog_pk)
    blog_content_type = ContentType.objects.get_for_model(blog)
    comments = Comment.objects.filter(content_type=blog_content_type,object_id=blog.pk)
    if not request.COOKIES.get('blog_%s_read'%blog_pk):
        if ReadNum.objects.filter(blog=blog).count():
            # 存在记录
            readnum = ReadNum.objects.get(blog=blog)
        else:
            readnum = ReadNum(blog = blog)
        readnum.read_num += 1
        readnum.save()

    context = {}
    context['blog'] = blog
    context['comments'] = comments
    context['comment_form'] = CommentForm(initial={'content_type':blog_content_type.model,'object_id':blog_pk})
    response =  render(request, 'blog_detail.html', context)
    response.set_cookie('blog_%s_read'%blog_pk,'true',max_age=60)
    return response

def blog_with_type(request,blog_type_pk):
    context = {}
    blog_type = get_object_or_404(BlogType,pk=blog_type_pk)
    context['blogs'] = Blog.objects.filter(blog_type=blog_type)
    context['blog_type'] = blog_type
    return render(request,'blog_with_type.html',context)

