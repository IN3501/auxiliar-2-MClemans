from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('peliculas/', views.peliculas, name='peliculas'),
	path('nombres/', views.nombres, name='nombres'),

]