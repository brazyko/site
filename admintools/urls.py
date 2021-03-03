from django.urls import path
from .views import *

app_name = 'admintools'

urlpatterns = [
    path('',admintools,name='admintools'),
    path('usermanagment/',usermanagment,name='usermanagment'),
    path('ordersadmin/',orders_administration,name='orders_admin'),
    path('ordersadmin/confirm-ordr-formed-<ref>',orders_shipping_administration_formed,name='orders_shipping_administration_formed'),
    path('ordersshipadmin/',orders_shipping_administration,name='orders_shipping_admin'),
    path('ordersshipadmin/confirm-passed-to-ship-<ref>',orders_shipping_administration_confirm,name='orders_shipping_admin_confirm'),
]