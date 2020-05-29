"""URL Patterns for the CART """
from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    #home
    path('', views.cart_detail, name='cart_detail'),
    #add cart item.
    path('add/<int:product_id>/', views.cart_add, name='cart_add'),
    #remove cart item.
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
]