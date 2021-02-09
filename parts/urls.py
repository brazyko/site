from django.urls import path
from .views import *
app_name = 'parts'
urlpatterns = [
    path('',partslist,name='partslist'),
    path('search',partSearch,name='part_search'),
    path('<id>',partdetail.as_view(),name='partdetail'),
]