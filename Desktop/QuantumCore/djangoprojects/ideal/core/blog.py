from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,View,CreateView
from django.views.generic.edit import DeleteView,UpdateView
from django.contrib.auth.mixins import UserPassesTestMixin,LoginRequiredMixin
from django.http import HttpResponse
from .models import Blog
from .forms import BlogForm

class CreateBlog(LoginRequiredMixin,UserPassesTestMixin,CreateView) :
    login = 'login'
    template_name = 'create_blog.html'
    form_class = BlogForm
    model = Blog

    


class DeleteBlog(LoginRequiredMixin,UserPassesTestMixin,DeleteView)  :
    login = 'login'
    template_name = 'delete_blog.html'
    model = Blog
    
    def test_func(self) :
        return self.request.user ==  self.get_object().author


class  UpdateBlog(LoginRequiredMixin,UserPassesTestMixin,UpdateView)   :

    login = 'login'
    template_name = 'delete_blog.html'
    model = Blog
    
    def test_func(self) :
        return self.request.user ==  self.get_object().author



class BlogDetail(View) :
    model = Blog
    get_blog_type_templates = {'TV':'detail_blog_tv.html','XCHANGE' :  'detail_blog_xchange.html',
    'IDEAL' : 'detail_blog_ideal.html'}
    def get(self,request,*args,**kwargs) :
        _slug  = kwargs.get('slug',None)
        if _slug :
            blog = get_object_or_404(self.model,slug = _slug)
            template = self.get_blog_type_templates.get(blog.blog_type,'IDEAL')
        else : return HttpResponse('invalid request')
        return render(request,template,locals())  
        

#class BlogList(ListView)        