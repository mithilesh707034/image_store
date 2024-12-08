from rest_framework import serializers
from .models import *


class WebsiteFrontImageSerializers(serializers.Serializer):
    image=serializers.ImageField(max_length=None,use_url=True)
    def create(self, validated_data):
        return WebsiteFrontImage.objects.create(**validated_data)
    
class WebsiteBlogImageSerializers(serializers.Serializer):
    image=serializers.ImageField(max_length=None,use_url=True)
    def create(self, validated_data):
        return WebsiteBlogImage.objects.create(**validated_data)
    
class CatalogueLogoSerializers(serializers.Serializer):
    image=serializers.ImageField(max_length=None,use_url=True)
    def create(self, validated_data):
        return CatalogueLogo.objects.create(**validated_data)
    
class CatalogueImageSerializers(serializers.Serializer):
    image=serializers.ImageField(max_length=None,use_url=True)
    def create(self, validated_data):
        return CatalogueImage.objects.create(**validated_data)