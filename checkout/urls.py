from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name="checkout"),
    path('order_confirmed/<order_number>', views.order_confirmed, name="order_confirmed"),
]
