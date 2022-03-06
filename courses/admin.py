from django.contrib import admin

from .models import Course, Payment

@admin.register(Course)
class coursesAdmin(admin.ModelAdmin):
    list_display=('coTitle',)
    list_filter=('coTitle',)
    search_fields=('coTitle',)
@admin.register(Payment)
class paymentAdmin(admin.ModelAdmin):
    list_display=('course', 'paDate', 'Estudiante')
    list_filter=('paDate',)
    search_fields=('paDate',)

    def Estudiante(self, obj):
        return str(obj.user.first_name) + " " + str(obj.user.last_name)
