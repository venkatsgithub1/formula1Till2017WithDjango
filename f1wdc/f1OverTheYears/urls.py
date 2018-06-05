from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('f1_by_year/', views.f1_by_year, name="f1_by_year"),
    path('f1_data/', views.f1_data, name="f1_data")
]