from django.urls import path
from . import views

urlpatterns = [
    path('', views.doodles_collection, name="doodles"),
    path('<int:doodle_id>/', views.dooddle_page, name="dooddle_page"),
    path('search/', views.doodles_search, name="search"),

]
