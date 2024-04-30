from django.contrib import admin
from apps.users.models import Users

@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    list_display = ('phone', 'age', 'created_at')
