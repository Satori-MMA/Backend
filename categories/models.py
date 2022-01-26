from django.db.models import (
    CASCADE,
    CharField,
    Model
)

from django.utils.translation import gettext_lazy as _

# Create your models here.

class Category(Model): 
    catName = CharField(
        _('Nombre'),
        max_length=255,
        null=True,
        blank=False,
        help_text= _('Nombre de la categoria'),
        default= _('General')
    )

    class Meta:
        verbose_name = _('Categoria')
        verbose_name_plural = _('Categorias')


    def __str__(self) -> str:
        return self.catName