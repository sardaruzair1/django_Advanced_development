from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('word/', views.index2, name='index2'),
    path('counter/', views.counter, name='counter')
]
