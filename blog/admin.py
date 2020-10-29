from django.contrib import admin
from blog.models import Blog, BlogType, BlogSource,ReadNum
# Register your models here.
@admin.register(BlogType)
class BlogTypeadmin(admin.ModelAdmin):
    list_display = ('id','type_name')

@admin.register(BlogSource)
class BlogSourcedmin(admin.ModelAdmin):
    list_display = ('id','source','sour_url')

@admin.register(ReadNum)
class BlogSourcedmin(admin.ModelAdmin):
    list_display = ('id','read_num','blog')

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','author','id','get_read_num','blog_type','create_time','last_updated_time','is_deleted')
    ordering = ('id',) # 倒序即-id