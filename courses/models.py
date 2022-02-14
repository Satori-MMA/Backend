from django.db import models
from django.db.models import (
    CASCADE,
    Model,
    ForeignKey
)
from django.db.models.deletion import DO_NOTHING
from django.utils.translation import gettext_lazy as _
from categories.models import Category
from users.models import UserStori

class Course(Model):
    """Cousers model."""
    coTitle = models.CharField(_('Titulo'), max_length=255,blank=False)
    coDescription = models.CharField(_('Descripción'), max_length=255,blank=False)
    coImage = models.CharField(_('Imagen'),max_length=255,blank=False)
    coPrice = models.FloatField(_('Precio'),blank=False)
    is_active = models.BooleanField(_('Activo'), default=True)
    members = models.ManyToManyField(UserStori, through='Payment')

    #Relaciones
    category = ForeignKey(
        Category,
        verbose_name= _('Categoria'),
        related_name='courses',
        on_delete=CASCADE,
        help_text=_('Categoria del curso')
    )

    class Meta:
        verbose_name = _('Curso')
        verbose_name_plural = _('Cursos')

    def __str__(self):
        return self.coTitle
class Payment(Model):
    user = ForeignKey(
        UserStori,
        verbose_name= _('Usuario'),
        on_delete=DO_NOTHING,
    )
    course = ForeignKey(
        Course,
        verbose_name= _('Curso'),
        on_delete=DO_NOTHING,
    )
    paDate = models.DateField(_('Fecha'),blank=False)

    class Meta:
        verbose_name = _('Pago')
        verbose_name_plural = _('Pagos')