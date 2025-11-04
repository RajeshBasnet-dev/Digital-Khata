from django.urls import path
from . import views

app_name = 'dashboard'
urlpatterns = [
    # Traditional views
    path('', views.dashboard, name='dashboard'),
    
    # API endpoints
    path('api/data/', views.dashboard_data, name='dashboard-data'),
]