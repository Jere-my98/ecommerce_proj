from django.urls import path
from . import views

urlpatterns = [
    #URL for Store Home
    path('', views.store_home, name='store_home'),

    # URLs for Products
    path('products/', views.product_list, name='product_list'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),

    # URLs for Categories
    path('categories/', views.category_list, name='category_list'),
    path('categories/<int:pk>/', views.category_detail, name='category_detail'),

    # URLs for Orders
    path('orders/', views.order_list, name='order_list'),
    path('orders/<int:pk>/', views.order_detail, name='order_detail'),

    # URL for Cart
    # path('cart/', views.cart_detail, name='cart_detail'),

    # URLs for Addresses
    # path('addresses/', views.address_list, name='address_list'),
    # path('addresses/<int:pk>/', views.address_detail, name='address_detail'),
]
