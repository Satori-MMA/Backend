# Generated by Django 3.2.9 on 2022-03-06 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_remove_payment_monthlypayment'),
        ('monthly_payments', '0002_monthlypayment_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthlypayment',
            name='payment',
            field=models.ForeignKey(db_column='payment_id', default='', help_text='Pago de mensualidad', on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='courses.payment', verbose_name='payment'),
        ),
    ]