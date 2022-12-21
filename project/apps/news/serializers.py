from .models import News, Comment, Tag, Category, Image, Video
from rest_framework import serializers


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'
        # extra_kwargs = {
        #     'id': {'read_only': True},
        #     'isActive': {'read_only': True},
        #     'created_at': {'read_only': True},
        #     'updated_at': {'read_only': True},
        # }


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        # extra_kwargs = {
        #     'id': {'read_only': True},
        #     'isActive': {'read_only': True},
        # }


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'
