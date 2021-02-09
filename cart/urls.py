from django.urls import path

from .views import *
app_name = 'shopping_cart'

urlpatterns = [
    path('', order_details,name='order_summary'),
    path('add-to-cart/<item_id>',add_to_cart,name ='add_to_cart'),
    path('item/delete/<item_id>',delete_from_cart,name='delete_from_cart'),
]