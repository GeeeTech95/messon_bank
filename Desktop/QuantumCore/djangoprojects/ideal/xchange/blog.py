from django.views.generic import ListView
from core.models import Blog


class News(ListView) :
    model = Blog
    template_name = 'blog-list-xchange.html' 
    context_object_name = 'blogs'
    def get_queryset(self,*args,**kwargs) :
        _all = self.model.objects.filter(blog_type = 'XCHANGE').order_by('-date')[:4]
        return _all