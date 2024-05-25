from django.urls import path
from .views import AdminCategoryListCreateAPIView

urlpatterns = [
    path('categories/', AdminCategoryListCreateAPIView.as_view(), name='admin-category-list-create'),
]
