from django.contrib import admin
from .models import UserStori
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _
from django.apps import apps

app = apps.get_app_config('graphql_auth')
for model_name, model in app.models.items():
    admin.site.register(model)

#admin.site.register(Users)
@admin.register(UserStori)
class UsersAdmin(DjangoUserAdmin):

    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

    """Define admin model for custom User model with no email field."""
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name','user_phone','user_address')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        #(_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser','groups', 'user_permissions')}),
       # (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name','last_name','email','user_phone','user_address','password1', 'password2','is_superuser','is_staff','is_active'),
        }),
    )
    #Lista en el menu
    list_display = ('email', 'first_name','is_active')
    list_filter = ('is_active',)
    #fields = ('first_name','last_name','email','password','is_superuser','is_staff','is_active')
    #exclude = ('is_active',)