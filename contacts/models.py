from django.db.models import (
    CharField,
    Model,
    EmailField,
    TextField
)


from django.utils.translation import gettext_lazy as _

class ContactSatori(Model):

    """Contact model."""
    name = CharField(_('Nombre'), max_length=150,blank=False)
    email = EmailField(_('Email'),max_length=255,blank=False)
    phone = CharField(_('Telefono'),max_length=15,blank=True)
    comment = TextField(_('Comentario'),max_length=255,blank=True)

    class Meta:
        verbose_name = _('Comentario')
        verbose_name_plural = _('Comentarios')

    def __str__(self):
        return self.name