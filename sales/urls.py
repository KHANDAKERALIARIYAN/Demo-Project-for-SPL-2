from django.urls import path
from . import views

app_name = 'sales'

urlpatterns = [
    path('', views.sale_list, name='sale_list'),
    path('add/', views.sale_create, name='sale_create'),
    path('<int:pk>/', views.sale_detail, name='sale_detail'),
    path('<int:pk>/edit/', views.sale_update, name='sale_update'),
    path('<int:pk>/delete/', views.sale_delete, name='sale_delete'),
    # path('<int:pk>/invoice/', views.generate_invoice, name='generate_invoice'),
] 