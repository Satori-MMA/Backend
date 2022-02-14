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
    leName = models.CharField(_('Name'), max_length=255,blank=False)
    leDescription = models.CharField(_('Description'), max_length=255,blank=False)
    leEvaluation = models.FloatField(_('Evaluation'),blank=False)
    leLinkVideo = models.CharField(_('Link Video'), max_length=255,blank=False)

    #Relaciones
    course = ForeignKey(
        Course,
        verbose_name=_('Course'),
        related_name='lessons',
        on_delete=CASCADE,
        help_text=_('Lessiones del curso')
    )

    class Meta:
        verbose_name = _('Lesson')
        verbose_name_plural = _('Lessons')

    def __str__(self):
        return self.leName