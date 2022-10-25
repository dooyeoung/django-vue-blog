from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpRequest

from typing import Any

from blog.models import Post, Category, Tag, Comment

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'category',
        'tag_list',
        'title',
        'description',
        'image',
        'created_at',
        'updated_at',
    )


    def tag_list(self, obj):
        return ','.join(
            tag.name for tag in obj.tags.all()
        )
        
    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).prefetch_related('tags')
    

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'description',
    )

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name',
    )

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'post',
        'short_content',
        'created_at',
        'updated_at',
    )
