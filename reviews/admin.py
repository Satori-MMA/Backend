from django.contrib import admin

from .models import Review

@admin.register(Review)
class review(admin.ModelAdmin):
    list_display=('opComment','opQualification', 'lesson')
    list_filter=('opQualification',)
    search_fields=('opQualification',)
