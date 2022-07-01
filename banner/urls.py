from django.urls import path
from . import views #importando o arquivo views do diretorio onde estamos

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('photo/<str:pk>', views.viewPhoto, name='photo'),
    path('add/', views.addPhoto, name='add'),
]