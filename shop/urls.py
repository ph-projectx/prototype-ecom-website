"""URL Pattern for Shop"""
from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    #home
    path('', views.product_list, name='product_list'),
    #product_list with category
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    #product_detail
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]