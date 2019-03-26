#from django.shortcuts import render
from rest_framework import viewsets

from sampleplugin.models import Menu_Item
from api.serializers import MenuItemSerializer


# Create your views here.

class MenuItemViewSet(viewsets.ModelViewSet):
    #queryset = Menu_Item.objects.all()
    queryset = Menu_Item.objects.filter(placeholder__page__publisher_is_draft=False)
    serializer_class = MenuItemSerializer