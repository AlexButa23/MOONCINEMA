# Generated by Django 4.1.2 on 2022-11-15 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bacend', '0002_film_imagine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rezervare',
            name='locuri',
            field=models.CharField(max_length=1550),
        ),
    ]