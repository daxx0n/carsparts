# Generated by Django 4.2.1 on 2023-05-20 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directories', '0009_publisher_alter_author_author_firstname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='author_firstname',
            field=models.CharField(default="Enter Author's name", max_length=15, verbose_name='Author Name'),
        ),
    ]