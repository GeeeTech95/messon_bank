from django.views import ListView
from core.models import Blog


class LatestNews(ListView) :
    model = Blog
    def get_queryset(self,*args,**kwargs) :
        _all = self.model.objects.filter(blog_type = 'XCHANGE').order_by('-date')[:4]
        return _all