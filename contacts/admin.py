from django.contrib import admin

# Register your models here.
from .models import ContactSatori
@admin.register(ContactSatori)

class contactAdmin(admin.ModelAdmin):
    list_display=('name',)
    list_filter=('name',)
    search_fields=('name',)