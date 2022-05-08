from django.contrib import admin
from .models import News, Comment, Tag, Category, Image, Video


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title']
    list_filter = ['created_at']
    ordering = ['-created_at']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['text', 'created_at']
    search_fields = ['text']
    list_filter = ['created_at']
    ordering = ['-created_at']


class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    ordering = ['name']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    ordering = ['name']


admin.site.register(News, NewsAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Image)
admin.site.register(Video)
