from django.contrib import admin
from account.models import *

# Register your models here.
@admin.register(User)
class adminUser(admin.ModelAdmin):
    pass
