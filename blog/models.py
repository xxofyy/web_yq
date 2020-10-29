from django.db import models
from django.db.models.fields import exceptions
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField



class BlogType(models.Model):
    type_name = models.CharField(max_length=15)

    def __str__(self):
        return self.type_name

class BlogSource(models.Model):
    source = models.CharField(max_length=25)
    sour_url = models.CharField(max_length=50)

    def __str__(self):
        return self.source

class Blog(models.Model):
    title = models.CharField(max_length=30)#长度限制30个字符
    content = RichTextUploadingField()
    blog_type = models.ForeignKey(BlogType,on_delete=models.DO_NOTHING,default=1)
    source = models.ForeignKey(BlogSource,on_delete=models.DO_NOTHING,default=1)
    create_time = models.DateTimeField(default=timezone.now)
    last_updated_time=models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING,default=1)
    is_deleted = models.BooleanField(default=False)

    def get_read_num(self):
        try:
            return self.readnum.read_num
        except exceptions.ObjectDoesNotExist:
            return 0

    def __str__(self):
        return 'Blog:%s'%self.title

class ReadNum(models.Model):
    read_num = models.IntegerField(default=0)
    blog = models.OneToOneField(Blog,on_delete=models.DO_NOTHING)

