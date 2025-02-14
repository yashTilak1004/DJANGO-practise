from django.urls import path
from . import views

urlpatterns = [
    path('',views.main,name='main'),
    path('home/', views.home, name='home'),
    path('home/details/<int:id>', views.details, name='details'),
]