from django.urls import path
from . import views
from .webhooks import webhook


urlpatterns = [
    path('', views.checkout, name="checkout"),
    path('order_confirmed/<order_number>', views.order_confirmed, name="order_confirmed"),
    path('wh/', webhook, name='webhook'),
]
