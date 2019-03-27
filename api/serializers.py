from rest_framework import serializers

from sampleplugin.models import Menu_Item
from blog.models import Post, Category

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu_Item
        fields = ['id', 'name', 'image', 'price', 'description', 'url', ]


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'date', 'category', 'content', ]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', ]