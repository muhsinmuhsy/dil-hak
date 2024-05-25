from django.shortcuts import render
from rest_framework.views import APIView
from .models import Category, Product, ProductVariant, Color, ColorImage
from .serializers import CategorySerializer,ProductSerializer, ProductVariantListSerializer, ColorImageSerializer, ColorSerializer
from rest_framework.response import Response
from rest_framework import status

class CategoryListCreateAPIView(APIView):
    def get(self, request, format=None):
        try:
            categories = Category.objects.all()
            if not categories:
                return Response({"message": "No category found"}, status=status.HTTP_204_NO_CONTENT)
            serializer = CategorySerializer(categories, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"error": f"Failed to retrieve Category: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def post(self, request, format=None):
        try:
            serializer = CategorySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": f"Failed to create category: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CategoryWithProductsAPIView(APIView):
    def get(self, request, format=None, category_id=None):        
        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)
        
        category_serializer = CategorySerializer(category, context={'request': request})
        products = Product.objects.filter(category=category)
        product_serializer = ProductSerializer(products, many=True, context={'request': request})
        
        category_data = category_serializer.data
        category_data['products'] = product_serializer.data

        for product_data in category_data['products']:
            product_id = product_data['id']
            variants = ProductVariant.objects.filter(product_id=product_id)
            variants_serializer = ProductVariantListSerializer(variants, many=True, context={'request': request})
            product_data['variants'] = variants_serializer.data
        
        response_data = {
            'category': category_data
        }
        
        return Response(response_data, status=status.HTTP_200_OK)

class ProductsWithVariantsListAPIView(APIView):
    def get(self, request, format=None):
        try:
            products = Product.objects.all()
            if not products.exists():
                return Response({"message": "No products found"}, status=status.HTTP_200_OK)

            products_and_variants_data = []
            for product in products:
                product_data = self.get_product_with_variants(product)
                products_and_variants_data.append(product_data)

            response_data = {'products': products_and_variants_data}
            return Response(response_data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": f"Failed to retrieve products: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get_product_with_variants(self, product):
        product_serializer = ProductSerializer(product)
        variants = ProductVariant.objects.filter(product=product)
        variants_serializer = ProductVariantListSerializer(variants, many=True)
        product_data = product_serializer.data
        product_data['variants'] = variants_serializer.data
        return product_data
    
    
class ProductWithVariantsListAPIView(APIView):
    def get(self, request, format=None, product_id=None):
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        
        final_data = []

        variants = product.variants.all()  # Access related ProductVariant instances using 'variants' related_name
        product_serializer = ProductSerializer(product)
        variants_serializer = ProductVariantListSerializer(variants, many=True)
        
        # Append variants data to product data
        product_data = product_serializer.data
        product_data['variants'] = variants_serializer.data
        
        final_data.append(product_data)

        return Response({"product":final_data}, status=status.HTTP_200_OK)
    
    
class ColorAPIView(APIView):
    def get(self, request):
        colors = Color.objects.all()
        serializer = ColorSerializer(colors, many=True)
        return Response(serializer.data)

    def post(self, request):
        try:
            product_id = request.data.get('product')
            name = request.data.get('name')
            images_data = request.data.get('images', [])

            color = Color.objects.create(product_id=product_id, name=name)

            for image_data in images_data:
                # Serialize each image data
                image_serializer = ColorImageSerializer(data=image_data)
                if image_serializer.is_valid():
                    # Save the image instance
                    color_image = image_serializer.save()
                    # Associate the created ColorImage with the Color instance
                    color.images.add(color_image)
                else:
                    return Response(image_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            serializer = ColorSerializer(color)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

{
    "product": 1,
    "name": "red",
    "images": [
        {
            "name": "c1"
        },
        {  
            "name": "c2"
        },
        {
            "name": "c3"
        }
    ]
}

class ColorImageAPIView(APIView):
    def get(self, request, format=None, colorimage_id=None):
        try:
            color_image = ColorImage.objects.get(id=colorimage_id)
        except ColorImage.DoesNotExist:
            return Response({"error": "Color Image not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ColorImageSerializer(color_image)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def delete(self, request, format=None, colorimage_id=None):
        try:
            color_image = ColorImage.objects.get(id=colorimage_id)
        except ColorImage.DoesNotExist:
            return Response({"error": "Color Image not found"}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            color_image.delete()
            return Response({"message":"Deleted Successfully"},status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ColorDeleteAPIView(APIView):
    def get(self, request, format=None, color_id=None):
        try:
            color = Color.objects.get(id=color_id)
        except Color.DoesNotExist:
            return Response({"error": "Color Image not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ColorSerializer(color)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    def delete(self, request, format=None, color_id=None):
        try:
            color = Color.objects.get(id=color_id)
        except Color.DoesNotExist:
            return Response({"error": "Color not found"}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            color.delete()
            return Response({"message":"Deleted Successfully"},status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
