from django.contrib import admin

from .models import Lesson, lessonUser

@admin.register(Lesson)
class lessonAdmin(admin.ModelAdmin):
    list_display=('leName',)
    list_filter=('leName',)
    search_fields=('leName',)
@admin.register(lessonUser)    
class lessonUserAdmin(admin.ModelAdmin):
    list_display=('user', 'lesson', 'taCheck')
    list_filter=('user',)
    search_fields=('user',)
