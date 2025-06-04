from django.urls import path
from . import views

app_name = 'lending'

urlpatterns = [
    path('', views.lending_list, name='lending_list'),
    path('add/', views.lending_create, name='lending_create'),
    path('<int:pk>/', views.lending_detail, name='lending_detail'),
    path('<int:pk>/edit/', views.lending_update, name='lending_update'),
    path('<int:pk>/delete/', views.lending_delete, name='lending_delete'),
    path('<int:pk>/return/', views.lending_return, name='lending_return'),
] 