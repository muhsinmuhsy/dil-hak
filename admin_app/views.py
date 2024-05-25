from django.shortcuts import render
from product_app.views import CategoryListCreateAPIView as BaseCategoryListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from auth_app.permissions import IsOrderAdmin, IsProductAdmin, IsSalesAdmin

# Create your views here.

class AdminCategoryListCreateAPIView(BaseCategoryListCreateAPIView):
    permission_classes = [IsAuthenticated, IsOrderAdmin | IsProductAdmin | IsSalesAdmin]
