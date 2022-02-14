from django.contrib import admin

from .models import Lesson

@admin.register(Lesson)
class lessonAdmin(admin.ModelAdmin):
    list_display=('leName',)
    list_filter=('leName',)
    search_fields=('leName',)
