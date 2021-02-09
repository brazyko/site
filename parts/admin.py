from django.contrib import admin
from .models import Product,Category,ProductImage,Product2
from mptt.admin import MPTTModelAdmin,DraggableMPTTAdmin
from .resources import Product2Resource
# Register your models here.

from import_export.admin import ImportExportModelAdmin

class CustomMPTTModelAdmin(DraggableMPTTAdmin):
    # specify pixel amount for this ModelAdmin only:
    prepopulated_fields={'slug':('name',)}
    mptt_level_indent = 50

admin.site.register(Category,CustomMPTTModelAdmin)

class ProductImageInline(admin.StackedInline):
    model = ProductImage
    max_num = 5
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    list_display = ["title","category","instock","price"]

admin.site.register(ProductImage)
admin.site.register(Product, ProductAdmin)


class Product2Admin(ImportExportModelAdmin):
    resource_class = Product2Resource
    list_display = ["index","producer","description","original","instock","price"]

admin.site.register(Product2, Product2Admin)