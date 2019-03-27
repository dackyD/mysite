#from django.shortcuts import render
from rest_framework import viewsets

from sampleplugin.models import Menu_Item
from blog.models import Post, Category
from api.serializers import MenuItemSerializer, PostSerializer, CategorySerializer


# Create your views here.

class MenuItemViewSet(viewsets.ModelViewSet):
    #queryset = Menu_Item.objects.all()
    queryset = Menu_Item.objects.filter(placeholder__page__publisher_is_draft=False)
    serializer_class = MenuItemSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer