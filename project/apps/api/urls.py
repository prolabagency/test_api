from apps.news.api import NewsViewSet, CommentViewSet, TagViewSet, CategoryViewSet, ImageViewSet, VideoViewSet
from apps.todos.api import TodoViewSet, CategoryViewSet as TodoCategoryViewSet
from rest_framework import routers
from django.urls import path, include


router = routers.DefaultRouter()
router.register('news', NewsViewSet)
router.register('comments', CommentViewSet)
router.register('tags', TagViewSet)
router.register('categories', CategoryViewSet)
router.register('images', ImageViewSet)
router.register('videos', VideoViewSet)
router.register('todos', TodoViewSet)
router.register('todo-categories', TodoCategoryViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('accounts/', include('rest_registration.api.urls')),
]