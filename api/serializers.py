from rest_framework import serializers

from sampleplugin.models import Menu_Item

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu_Item
        fields = ['id', 'name', 'image', 'price', 'description', 'url']