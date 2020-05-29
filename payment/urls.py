"""URL Patterns for Payment"""
from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    #process payment
    path('process/', views.payment_process, name='process'),
    #process payment done
    path('done/', views.payment_done, name='done'),
    #process payment canceled.
    path('canceled/', views.payment_canceled, name='canceled'),
]