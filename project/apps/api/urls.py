from apps.news.api import NewsViewSet, CommentViewSet, TagViewSet, CategoryViewSet, ImageViewSet, VideoViewSet
from apps.todos.api import TodoViewSet, CategoryViewSet as TodoCategoryViewSet
from rest_framework import routers, permissions
from django.urls import path, include, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


router = routers.DefaultRouter()
router.register('news', NewsViewSet)
router.register('comments', CommentViewSet)
router.register('tags', TagViewSet)
router.register('categories', CategoryViewSet)
router.register('images', ImageViewSet)
router.register('videos', VideoViewSet)
router.register('todos', TodoViewSet)
router.register('todo-categories', TodoCategoryViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="TEST API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="alimovtillo@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    # path('swagger(?P<format>\.json|\.yaml)/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('accounts/', include('rest_registration.api.urls')),
    path('', include(router.urls)),
]