from django.contrib import admin

# Register your models here.
from .models import Role

@admin.register(Role)
class roleAdmin(admin.ModelAdmin):
    list_display=('user', 'rol_name',)
    list_filter=('rol_name',)
    search_fields=('rol_name',)