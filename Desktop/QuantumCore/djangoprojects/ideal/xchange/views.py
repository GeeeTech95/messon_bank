from django.shortcuts import render
from django.views.generic import TemplateView
from core.models import Blog

class Index(TemplateView) :
    template_name = 'index-xchange.html'

    def get_context_data(self,*args,**kwargs) : 
        context = super(Index,self).get_context_data(*args,**kwargs) 
        context['blogs'] = Blog.objects.filter(blog_type = "XCHANGE").order_by('-date')
        return context
        

class About(TemplateView) :
    template_name = 'about-xchange.html'

class Services(TemplateView) :
    template_name = 'services-xchange.html'
         

class TOS(TemplateView) :
    template_name  = 'terms-of-service-xchange.html'

class Contact(TemplateView) :
    template_name = 'contact-xchange.html'