from django.contrib import admin
from .models import Product,Category,ProductImage
from mptt.admin import MPTTModelAdmin,DraggableMPTTAdmin
from .resources import ProductResource
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

class ProductAdmin(ImportExportModelAdmin):
    resource_class = ProductResource
    list_display = ["index","producer","description","original","instock","price"]

admin.site.register(Product, ProductAdmin)