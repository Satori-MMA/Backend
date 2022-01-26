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
    coTitle = models.CharField(_('Title'), max_length=255,blank=False)
    coDescription = models.CharField(_('Description'), max_length=255,blank=False)
    coImage = models.CharField(_('Image'),max_length=255,blank=False)
    coPrice = models.FloatField(_('Price'),blank=False)
    is_active = models.BooleanField(_('Activo'), default=True)
    members = models.ManyToManyField(UserStori, through='Payment')

    #Relaciones
    category = ForeignKey(
        Category,
        related_name='courses',
        on_delete=CASCADE,
        help_text=_('Id Categoria')
    )

    class Meta:
        verbose_name = _('Curso')
        verbose_name_plural = _('Cursos')

    def __str__(self):
        return self.coTitle
class Payment(Model):
    user = ForeignKey(
        UserStori,
        on_delete=DO_NOTHING,
    )
    course = ForeignKey(
        Course,
        on_delete=DO_NOTHING,
    )
    paDate = models.DateField(_('Fecha'),blank=False)

    class Meta:
        verbose_name = _('Payment')
        verbose_name_plural = _('Payments')