# Generated by Django 4.1.2 on 2022-11-04 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bacend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='imagine',
            field=models.CharField(default='./', max_length=50),
            preserve_default=False,
        ),
    ]
