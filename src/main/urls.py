from django.urls import path
from . import views


# Set your urls here.

urlpatterns = [
    path('index/', views.index, name='index'),
    path('', views.login_user, name='login'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register, name='register'),
]


