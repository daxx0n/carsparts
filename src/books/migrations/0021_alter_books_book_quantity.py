# Generated by Django 4.2.1 on 2023-06-21 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0020_books_is_active_alter_books_book_page_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='book_quantity',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Book quantity'),
        ),
    ]