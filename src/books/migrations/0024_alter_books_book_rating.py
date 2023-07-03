# Generated by Django 4.2.1 on 2023-06-21 20:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0023_alter_books_book_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='book_rating',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)], verbose_name='Book rating'),
        ),
    ]