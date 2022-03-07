from django.contrib import admin

from .models import MonthlyPayment

@admin.register(MonthlyPayment)
class monthyPayment(admin.ModelAdmin):
    list_display=('moStartDate','moFinishDate', 'user')
    list_filter=('moType',)
    search_fields=('moType',)

    # def Estudiante(self, obj):
    #     return str(obj.user.first_name) + " " + str(obj.user.last_name)

