from django.shortcuts import render
from product_app.views import CategoryListCreateAPIView as BaseCategoryListCeateAPIView
from rest_framework.permissions import IsAuthenticated
from auth_app.permissions import IsCustomer

# Create your views here.

class CustomerCategoryListCreateAPIView(BaseCategoryListCeateAPIView):
    permission_classes = [IsAuthenticated, IsCustomer]
