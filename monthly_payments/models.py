from django.db import models

from django.db.models import (
    CASCADE,
    Model,
    ForeignKey
)

from courses.models import Payment
from django.utils.translation import gettext_lazy as _

class MonthlyPayment(Model):
    """MonthlyPayments Model"""
    moStartDate = models.DateField(_('Fecha Inicio'),blank=False)
    moFinishDate = models.DateField(_('Fecha Fin'),blank=False)
    moType = models.CharField(_('Tipo de Mensualidad'), max_length=255,blank=False)

    #Relaciones
    payment = ForeignKey(
        Payment,
        verbose_name= _('payment'),
        related_name='payments',
        on_delete=CASCADE,
        default="",
        db_column='payment_id',
        help_text=_('Pago de mensualidad')
    )
    class Meta:
        verbose_name = _('Mensualidad')
        verbose_name = _('Mensualidades')
    
    def __str__(self):
        return self.moType
