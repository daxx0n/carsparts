# Generated by Django 4.2.1 on 2023-07-12 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_order_phone_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Новый', 'NEW'), ('Оформлен', 'OFORMLEN'), ('В работе', 'ATWORK'), ('Выдан', 'VYDAN'), ('Отеменен', 'CLOSED')], default='NEW', max_length=8),
        ),
    ]