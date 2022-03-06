from django.contrib import admin

from .models import MonthlyPayment

@admin.register(MonthlyPayment)
class monthyPayment(admin.ModelAdmin):
    list_display=('moStartDate','moFinishDate', 'Estudiante')
    list_filter=('moType',)
    search_fields=('moType',)

    def Estudiante(self, obj):
        return str(obj.payment.user.first_name) + " " + str(obj.payment.user.last_name)

    # payment_user_first_name.admin_order_field = 'payment__user_first_name'
