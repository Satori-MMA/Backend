# Generated by Django 3.2.9 on 2022-01-28 02:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol_name', models.CharField(choices=[('STUDENT', 'Student'), ('TEACHER', 'Teacher')], help_text='Tipo de usuario', max_length=8, null=True, verbose_name='Rol')),
                ('user', models.ForeignKey(help_text='Usuario', on_delete=django.db.models.deletion.CASCADE, related_name='rol_user', to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
        ),
    ]
