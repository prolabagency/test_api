from .models import Category, Todo
from .serializers import CategorySerializer, TodoSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.filter(isActive=True)
    serializer_class = CategorySerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name']
    pagination_class = PageNumberPagination


class TodoViewSet(ModelViewSet):
    queryset = Todo.objects.filter(isActive=True)
    serializer_class = TodoSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['created_at']
    pagination_class = PageNumberPagination

