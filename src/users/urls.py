from django.urls import path
from . import views


# Set your urls here.

urlpatterns = [
    path('users/', views.view_users, name='users'),
    path('user_profile/', views.user_profile, name='user_profile'),
]


