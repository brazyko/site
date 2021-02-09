from django.urls import path
from .views import *
app_name = 'users'
urlpatterns = [
    path('register/',register,name='register'),
    path('login/',login_user,name='login'),
    path('logout/',logout_user,name='logout'),
    path('myprofile/',profile,name = 'myprofile'),
]