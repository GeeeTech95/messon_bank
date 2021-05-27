from django.db import models
from django.contrib.auth.models   import AbstractUser
from django.utils.text import  slugify


class User(AbstractUser) :
    
    def get_path(instance,filename) :
        filename = "{}.{}".format(instance.name,filename.split('.')[1])
        return "users/dp/{}".format(filename)
    
    name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length = 30,blank = False,null = False)
    picture = models.FileField(upload_to = get_path)
    referals = models.ManyToManyField('self',symmetrical=False,blank = True)

    def __str__(self)  :
        return self.username

    def save(self,*args,**kwargs) :
        self.slug = slugify(self.name) 
        super(User,self).save(*args,**kwargs)


class Dashboard(models.Model) :
    pass

class NewsLaterSubscriber(models.Model) :
    email = models.EmailField(blank = False)  

    def __str__(self)  :
        return self.email
