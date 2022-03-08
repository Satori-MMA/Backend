from django.db import models

from django.db.models import (
    CASCADE,
    Model,
    ForeignKey
)
from users.models import UserStori
from lessons.models import Lesson
from .choices import QUALIFICATION
from django.utils.translation import gettext_lazy as _

class Review(Model):
    """MonthlyPayments Model"""
    opComment = models.CharField(_('Comentario'), max_length=255, blank=False)
    opQualification = models.CharField(_('Calificación de la lección'), max_length=255, choices=QUALIFICATION)

     #Relaciones
    user = ForeignKey(
        UserStori,
        verbose_name= _('Usuario'),
        related_name='Usuarios',
        on_delete=CASCADE,
        default="",
        help_text=_('Estudiante')
    )
    lesson = ForeignKey(
        Lesson,
        verbose_name= _('Leccion'),
        related_name='Lecciones',
        on_delete=CASCADE,
        default="",
        help_text=_('Leccion')
    )

    class Meta:
        verbose_name = _('Reseña')
        verbose_name_plural = _('Reseñas')
    
    def __str__(self):
        return self.opQualification