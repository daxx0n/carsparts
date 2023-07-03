# Generated by Django 4.2.1 on 2023-06-21 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0015_alter_books_book_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='book_cover',
            field=models.TextField(blank=True, max_length=5, null=True, verbose_name='Cover'),
        ),
        migrations.AddField(
            model_name='books',
            name='book_isbn',
            field=models.CharField(blank=True, max_length=17, null=True, verbose_name='ISBN'),
        ),
        migrations.AddField(
            model_name='books',
            name='book_page',
            field=models.PositiveIntegerField(blank=True, max_length=5, null=True, verbose_name='Pages'),
        ),
        migrations.AddField(
            model_name='books',
            name='book_weight',
            field=models.PositiveIntegerField(blank=True, max_length=4, null=True, verbose_name='Weight'),
        ),
        migrations.AlterField(
            model_name='books',
            name='book_year',
            field=models.PositiveIntegerField(blank=True, max_length=4, null=True, verbose_name='Year'),
        ),
    ]