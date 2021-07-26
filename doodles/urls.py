from django.urls import path
from . import views

urlpatterns = [
    path('', views.doodles_collection, name="doodles"),
    path('<int:doodle_id>/', views.dooddle_page, name="dooddle_page"),
    path('search/', views.doodles_search, name="search"),
    path('add/', views.add_doodle, name='add_doodle'),
    path('edit/<int:doodle_id>/', views.edit_doodle, name='edit_doodle'),
    path('delete/<int:doodle_id>/',
         views.delete_doodle,
         name='delete_doodle'),

]
