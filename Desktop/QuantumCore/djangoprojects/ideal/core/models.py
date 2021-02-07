
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
import datetime

class Users(AbstractUser) :
    pass


class Blog(models.Model) :
    def get_path(instance,filename) :
        ext  = filename.split('.')[1]
        return "{}.{}".format(instance.slug,ext)

    type_choices  = (('TV','TV'),('XCHANGE','XCHANGE'),('IDEAL','IDEAL')) 
    title = models.CharField(max_length  = 30)
    author = models.ForeignKey(get_user_model(),on_delete = models.CASCADE)
    blog_type = models.CharField(max_length  = 20,choices = type_choices) 
    picture = models.FileField(upload_to = get_path)
    content = models.TextField()
    slug = models.CharField(max_length = 50)
    date =  models.DateTimeField(auto_now_add = True)

    def save(self,*args,**kwargs) :
        self.slug  = slugify(self.title,str(datetime.datetime.now()))
        super(Blog,self).save(*args,**kwargs)
        return

    def __str__(self) :
        return self.title    