# Generated by Django 4.2.1 on 2023-05-09 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_topping'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Pizza',
        ),
        migrations.DeleteModel(
            name='Topping',
        ),
    ]
