from django.contrib import admin
from apps.accounts.models import CustomUser

# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_active')
    search_fields = ('email',)
    ordering = ('id',)

