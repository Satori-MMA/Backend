from django.db.models import (
    CASCADE,
    CharField,
    Model,
    TextChoices,
    ForeignKey
)

from users.models import UserStori
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Role(Model):
    class type_roles(TextChoices):
        STUDENT = _("STUDENT"), _("Student")
        TEACHER = _("TEACHER"), _("Teacher")

    rol_name = CharField(
        max_length=8,
        choices=type_roles.choices,
        null=True,
        blank=True,
        help_text= _('tipo de usuario')
    )

    #Relaciones
    user = ForeignKey(
        UserStori,
        related_name= _('rol_user'),
        on_delete=CASCADE,
        help_text= _('Rol_User')
    )


    def __str__(self) -> str:
        return self.rol_name