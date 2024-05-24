from django.urls import path
from .views import CustomerCategoryListCreateView

urlpatterns = [
    path('categories/', CustomerCategoryListCreateView.as_view(), name='customer-category-list-create'),
]
