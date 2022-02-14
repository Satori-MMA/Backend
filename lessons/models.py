from django.db import models
from django.db.models import (
    CASCADE,
    Model,
    ForeignKey
)

from django.utils.translation import gettext_lazy as _
from courses.models import Course
class Lesson(Model):
    """ Lesson Model"""
    leName = models.CharField(_('Nombre'), max_length=255,blank=False)
    leDescription = models.CharField(_('Descripción'), max_length=255,blank=False)
    leEvaluation = models.FloatField(_('Evaluación'),blank=False)
    leLinkVideo = models.CharField(_('Link de video'), max_length=255,blank=False)
    is_active = models.BooleanField(_('Activo'), default=True)

    #Relaciones
    course = ForeignKey(
        Course,
        verbose_name=_('Curso'),
        related_name='lessons',
        on_delete=CASCADE,
        help_text=_('Lecciones del curso')
    )

    class Meta:
        verbose_name = _('Leccion')
        verbose_name_plural = _('Lecciones')

    def __str__(self):
        return self.leName