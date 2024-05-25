from django.urls import path
from .views import CustomerCategoryListCreateAPIView

urlpatterns = [
    path('categories/', CustomerCategoryListCreateAPIView.as_view(), name='customer-category-list-create'),
]
