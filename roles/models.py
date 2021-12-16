from django.db.models import (
    CASCADE,
    CharField,
    Model,
    TextChoices,
    ForeignKey
)

from users.models import ExtendUser

# Create your models here.

class Role(Model):
    class type_roles(TextChoices):
        STUDENT = "STUDENT", "Student"
        TEACHER = "TEACHER", "Teacher"

    rol_name = CharField(
        max_length=7,
        choices=type_roles.choices,
        null=True,
        blank=True,
        help_text='tipo de usuario'
    )

    #Relaciones
    user = ForeignKey(
        ExtendUser,
        related_name='rol_user',
        on_delete=CASCADE,
        help_text='Rol_User',
    )


    def __str__(self) -> str:
        return self.rol_name