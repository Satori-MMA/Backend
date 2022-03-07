from django.db import models

from django.db.models import (
    CASCADE,
    Model,
    ForeignKey
)
from lessons.models import Lesson
from .choices import QUALIFICATION
from django.utils.translation import gettext_lazy as _

class Review(Model):
    """MonthlyPayments Model"""
    opComment = models.CharField(_('Comentario'), max_length=255, blank=False)
    opQualification = models.CharField(_('Calificación de la lección'), max_length=255, choices=QUALIFICATION)

     #Relaciones
    lesson = ForeignKey(
        Lesson,
        verbose_name= _('lesson'),
        related_name='lessons',
        on_delete=CASCADE,
        default="",
        help_text=_('Estudiante')
    )

    class Meta:
        verbose_name = _('Reseña')
        verbose_name_plural = _('Reseñas')
    
    def __str__(self):
        return self.opQualification