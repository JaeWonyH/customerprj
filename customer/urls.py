from django.urls import path
from . import views

urlpatterns = [

    path('', views.customer_list, name='customer_list'),
    path('customer/<int:pk>', views.customer_detail, name='customer_detail'),
    # http://localhost:8000/blog/post/new
    path('post/new/', views.customer_new_modelform, name='customer_new'),


]