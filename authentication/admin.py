from django.contrib import admin
from .models import User
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'mobile', "created", "modified"]
    search_fields = ['id', 'mobile']
