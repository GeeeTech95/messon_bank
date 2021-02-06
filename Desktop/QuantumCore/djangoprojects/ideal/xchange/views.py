from django.shortcuts import render
from django.views.generic import TemplateView
from core.models import Blog

class Index(TemplateView) :
    template_name = 'index-xchange.html'

    def context_data(self,args,**kwargs) : 
        context = super(self,Index).get_context_data(*args,**kwargs) 
        context['blogs'] = Blog.objects.filter(blog_type = "XCHANGE").order_by('-date')
        return context
        




