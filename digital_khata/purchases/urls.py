from django.urls import path
from . import views

app_name = 'purchases'
urlpatterns = [
    path('', views.bill_list, name='bill_list'),
    path('create/', views.bill_create, name='bill_create'),
    path('<int:pk>/update/', views.bill_update, name='bill_update'),
    path('<int:pk>/delete/', views.bill_delete, name='bill_delete'),
]