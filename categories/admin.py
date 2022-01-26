from django.contrib import admin

# Register your models here.
from .models import Category

@admin.register(Category)
class categoryAdmin(admin.ModelAdmin):
    list_display = ('catName',)
    list_filter=('catName',)
    search_fields=('catName',)