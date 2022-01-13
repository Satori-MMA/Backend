from django.db import models
from django.db.models import (
    CASCADE,
    Model,
    ForeignKey
)
from django.db.models.deletion import DO_NOTHING
from django.utils.translation import gettext_lazy as _
from users.models import UserStori

class Course(Model):
    """Cousers model."""
    coTitle = models.CharField(_('Titulo'), max_length=255,blank=False)
    coDescription = models.CharField(_('Description'), max_length=255,blank=False)
    coImage =models.CharField(_('Email'),max_length=255,blank=False)
    coPrice = models.CharField(_('Precio'),max_length=255,blank=False)
    members = models.ManyToManyField(UserStori, through='Payment')
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