from django.shortcuts import render
from django.views.generic import DetailView

from blog.models import Post

# Create your views here.
class PostDV(DetailView):
    model = Post
    template_name: str = 'blog/post_detail.html'