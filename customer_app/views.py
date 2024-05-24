from product_app.views import CategoryListCeateView as BaseCategoryListCeateView
from rest_framework.permissions import IsAuthenticated
from auth_app.permissions import IsCustomer

# Create your views here.

class CustomerCategoryListCreateView(BaseCategoryListCeateView):
    permission_classes = [IsAuthenticated, IsCustomer]
