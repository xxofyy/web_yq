from django.db import models

# Create your models here.

class AppName(models.Model):
    app_href= models.CharField(max_length=20,default='#')
    app_name = models.CharField(max_length=20)

    def __str__(self):
        return self.app_name