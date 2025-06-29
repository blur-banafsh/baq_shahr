from django.contrib import admin
from home.models import *

# Register your models here.


@admin.register(Category)
class adminCategory(admin.ModelAdmin):
    pass


@admin.register(Item)
class adminItem(admin.ModelAdmin):
    pass


@admin.register(CategoryForGallery)
class adminItem(admin.ModelAdmin):
    pass


@admin.register(Gallery)
class adminItem(admin.ModelAdmin):
    pass
