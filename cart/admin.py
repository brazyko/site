from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(CartItem)

class OrderAdmin(admin.ModelAdmin):
    list_display=['ref_code','owner','order_status','date_ordered']
admin.site.register(Order,OrderAdmin)

admin.site.register(ShippingData)