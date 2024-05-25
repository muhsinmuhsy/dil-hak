from django.urls import path
from .views import CategoryListCreateAPIView, ProductsWithVariantsListAPIView, ProductWithVariantsListAPIView, CategoryWithProductsAPIView, ColorAPIView, ColorDeleteAPIView, ColorImageAPIView

urlpatterns = [
    path('categories/', CategoryListCreateAPIView.as_view(), name='category-list-create'),
    path('category/<int:category_id>/products/', CategoryWithProductsAPIView.as_view(), name='category-wth-products'),
    path('products/', ProductsWithVariantsListAPIView.as_view(), name='products-wth-variants-list'),
    path('product/<int:product_id>/variants/', ProductWithVariantsListAPIView.as_view(), name='product-wth-variants-list'),
    path('colors/', ColorAPIView.as_view(), name='color'),
    path('color/<int:color_id>/delete/', ColorDeleteAPIView.as_view(), name='color-delete'),
    path('colorimage/<int:colorimage_id>/delete/', ColorImageAPIView.as_view(), name='colorimage-delete'),
]