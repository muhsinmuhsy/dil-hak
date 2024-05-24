from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None
    
    class Meta:
        model = Category
        fields = '__all__'
                                                                                      
                                                                  
class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = '__all__'


class ColorImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColorImage
        fields = ('id', 'image', 'name')


class ColorSerializer(serializers.ModelSerializer):
    images = ColorImageSerializer(many=True, read_only=True)

    class Meta:
        model = Color
        fields = ('id', 'product', 'name', 'images')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        

class ProductVariantListSerializer(serializers.ModelSerializer):
    size = SizeSerializer()
    color = ColorSerializer()

    class Meta:
        model = ProductVariant
        fields = '__all__'
        
class ProductVariantAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = '__all__'