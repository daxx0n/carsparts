# Generated by Django 4.2.1 on 2023-05-19 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=15, verbose_name='Author')),
                ('author2_name', models.CharField(blank=True, max_length=15, null=True, verbose_name='Author2')),
            ],
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series_name', models.CharField(blank=True, max_length=15, null=True, verbose_name='Series')),
            ],
        ),
        migrations.DeleteModel(
            name='City',
        ),
    ]
