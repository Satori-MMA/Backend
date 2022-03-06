# Generated by Django 3.2.9 on 2022-03-06 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MonthlyPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moStartDate', models.DateField(verbose_name='Fecha Inicio')),
                ('moFinishDate', models.DateField(verbose_name='Fecha Fin')),
                ('moType', models.CharField(max_length=255, verbose_name='Tipo de Mensualidad')),
                ('payment', models.ForeignKey(db_column='payment_id', default='', help_text='Pago de mensualidad', on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='courses.payment', verbose_name='payment')),
            ],
            options={
                'verbose_name': 'Mensualidad',
                'verbose_name_plural': 'Mensualidades',
            },
        ),
    ]
