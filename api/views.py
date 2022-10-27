from django.http import JsonResponse
from django.views.generic.list import BaseListView
from django.views.generic.detail import BaseDetailView
from django.views import View

from blog.models import Post, Category, Tag
from api.utils import obj_to_post, prev_next_post


class ApiPostLV(BaseListView):
    # model = Post
    
    def get_queryset(self):
        paramCate = self.request.GET.get('category')
        paramTag = self.request.GET.get('tag')
        if paramCate:
            qs = Post.objects.filter(
                category__name__iexact=paramCate
            )
        elif paramTag:
            qs = Post.objects.filter(
                tags__name__iexact=paramTag
            )
        else:
            qs = Post.objects.all()
        return qs
    
    def render_to_response(self, context, **response_kwargs):
        qs = context['object_list']
        postList = [obj_to_post(obj, False) for obj in qs]
        return JsonResponse(data=postList, safe=False, status=200)
    

class ApiPostDV(BaseDetailView):
    model = Post
  
    def render_to_response(self, context, **response_kwargs):  
        obj = context['object']
        post = obj_to_post(obj)
        prevPost, nextPost = prev_next_post(obj)
        jsonData = {
            'post': post,
            'nextPost': nextPost,
            'prevPost': prevPost,
        }
        return JsonResponse(
            data=jsonData,
            safe=True,
            status=200,
        )


class ApiCateTagView(View):
    def get(self, request, *args, **kwargs):
        cateList = Category.objects.all()
        tagList = Tag.objects.all()
        
        cateList = [cate.name for cate in cateList]
        tagList = [tag.name for tag in tagList]
        
        jsonData = {
            'cateList': cateList,
            'tagList': tagList,
        }
        return JsonResponse(data=jsonData, safe=True, status=200)
    
class ApiPostLikeDv(BaseDetailView):
    model = Post
    
    def render_to_response(self, context, **response_kwargs):
        obj = context['object']
        obj.like += 1
        obj.save()
        
        return JsonResponse(data=obj.like, safe=False, status=200)