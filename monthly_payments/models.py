from django.db import models

from django.db.models import (
    CASCADE,
    Model,
    ForeignKey
)

from users.models import UserStori
from .choices import TYPE_MONTHLY_PAYMENT
from django.utils.translation import gettext_lazy as _

class MonthlyPayment(Model):
    """MonthlyPayments Model"""
    moStartDate = models.DateField(_('Fecha Inicio'),blank=False)
    moFinishDate = models.DateField(_('Fecha Fin'),blank=False)
    moType = models.CharField(_('Tipo de Mensualidad'), max_length=255, choices=TYPE_MONTHLY_PAYMENT)
    moPrice = models.FloatField(_('Precio Mensualidad'),blank=False)

    #Relaciones
    user = ForeignKey(
        UserStori,
        verbose_name= _('user'),
        related_name='users',
        on_delete=CASCADE,
        default="",
        help_text=_('Estudiante')
    )
    class Meta:
        verbose_name = _('Mensualidad')
        verbose_name_plural = _('Mensualidades')
    
    def __str__(self):
        return self.moType
