from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path("login/",  views.login, name="login"),
    path("logout/",  views.logout, name="logout"),
    path('post/<str:pk>', views.post, name='post'),
    path('counter/', views.counter,name='counter')
]
