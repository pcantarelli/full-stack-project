from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery, name="gallery"),
    path('<int:image_id>/', views.image, name="image"),

]
