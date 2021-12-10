from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.
class User(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class ExtendUser(AbstractUser):
    """User model."""
    first_name = models.CharField(_('Nombre'), max_length=150,blank=False)
    last_name = models.CharField(_('Apellido'), max_length=150,blank=False)
    email =models.EmailField(_('Email'),max_length=255,blank=False, unique=True)
    #password =models.CharField(_('Contraseña'), max_length=150,blank=False)
    is_active = models.BooleanField(_('Activo'),default=True)
    is_superuser = models.BooleanField(_('Super Usuario'),default=False)
    is_staff = models.BooleanField(_('Es personal'),default=False)
    created_at = models.DateTimeField(_('Fecha registro'),auto_now_add=True)
    updated_at = models.DateTimeField(_('Fecha actualización'),auto_now=True)

    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = User()

    #CASCADE-SET_NULL-PROTECT-SET-DO_NOTHING
    #father = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name=_('Padre'))

    class Meta:
        verbose_name = _('Usuario')
        verbose_name_plural = _('Usuarios')
        #Nombre a tabla
        #db_table = 'usuario'
        #indices
        #indexes = (models.Index(fields=('text','name')))
        #Claves primarias compuestas
        #unique_together = ('name','text')
        #Odenar -descendente
        #ordering = ('-created_at','name')
        #Clase que no se refleje en la base de datos
        #abstract = True


    def __str__(self):
        return self.email