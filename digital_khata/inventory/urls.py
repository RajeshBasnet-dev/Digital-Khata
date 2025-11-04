from django.urls import path
from . import views

app_name = 'inventory'
urlpatterns = [
    # Traditional views
    path('', views.product_list, name='product_list'),
    path('create/', views.product_create, name='product_create'),
    path('<int:pk>/update/', views.product_update, name='product_update'),
    path('<int:pk>/delete/', views.product_delete, name='product_delete'),
    
    # API endpoints
    path('api/products/', views.ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('api/products/<int:pk>/', views.ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-detail'),
    path('api/categories/', views.CategoryListCreateAPIView.as_view(), name='category-list-create'),
    path('api/categories/<int:pk>/', views.CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category-detail'),
]