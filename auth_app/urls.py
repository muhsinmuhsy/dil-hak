from django.urls import path, include
from auth_app.views import *
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('customer/', CustomerListCreateView.as_view(), name='user-list-create'),
    path('customer/<int:customer_id>/', CustomerDetailView.as_view(), name='user-detail'),
    path('customer/<int:customer_id>/verify-otp/', CustomerVerifyOTPView.as_view(), name='user-verify-otp'),
    path('customer/<int:customer_id>/regenerate-otp/', CustomerRegenerateOTPView.as_view(), name='user-regenerate-otp'),
    
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('user/customer/profile/add/', UserProfileCreateView.as_view()),
    
    path('product-admins/', ProductAdminListCreateView.as_view(), name='product_admin_list_create'),
    path('sales-admins/', SalesAdminListCreateView.as_view(), name='sales_admin_list_create'),
    path('order-admins/', OrderAdminListCreateView.as_view(), name='order_admin_list_create'),
    
    path('admin-login/', AdminLoginView.as_view(), name='admin-login'),
]
