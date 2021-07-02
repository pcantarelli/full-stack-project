from django.urls import path
from . import views

urlpatterns = [
    path('', views.doodles_collection, name="doodles")
]
