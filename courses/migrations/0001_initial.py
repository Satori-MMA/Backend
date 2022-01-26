# Generated by Django 3.2.9 on 2022-01-26 16:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coTitle', models.CharField(max_length=255, verbose_name='Titulo')),
                ('coDescription', models.CharField(max_length=255, verbose_name='Descripcion')),
                ('coImage', models.CharField(max_length=255, verbose_name='Imagen')),
                ('coPrice', models.FloatField(verbose_name='Precio')),
                ('is_active', models.BooleanField(default=True, verbose_name='Activo')),
                ('category', models.ForeignKey(help_text='Categoria del curso', on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='categories.category')),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paDate', models.DateField(verbose_name='Fecha')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='courses.course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Pago',
                'verbose_name_plural': 'Pagos',
            },
        ),
        migrations.AddField(
            model_name='course',
            name='members',
            field=models.ManyToManyField(through='courses.Payment', to=settings.AUTH_USER_MODEL),
        ),
    ]
