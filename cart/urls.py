from django.urls import path
from . import views

urlpatterns = [
    path("", views.cart, name="cart"),
    path("add/<item_id>/", views.add_to_cart, name="add_to_cart"),
    path("add_custom", views.add_custom_to_cart, name="add_custom_to_cart"),
    path("remove/<item_id>/", views.remove_from_cart, name="remove_from_cart"),
]
