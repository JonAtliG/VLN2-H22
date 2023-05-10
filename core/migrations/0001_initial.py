# Generated by Django 4.2.1 on 2023-05-10 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('img', models.CharField(blank=True, max_length=9999)),
                ('Bacon', models.BooleanField(default=False)),
                ('Chicken', models.BooleanField(default=False)),
                ('Ham', models.BooleanField(default=False)),
                ('Pepperoni', models.BooleanField(default=False)),
                ('Jalapeno', models.BooleanField(default=False)),
                ('Mushrooms', models.BooleanField(default=False)),
                ('Onion', models.BooleanField(default=False)),
                ('Paprika', models.BooleanField(default=False)),
                ('Pineapple', models.BooleanField(default=False)),
                ('Cheese', models.BooleanField(default=False)),
                ('Mozzarella', models.BooleanField(default=False)),
                ('Pepper_Cheese', models.BooleanField(default=False)),
                ('Yellow_Cheese', models.BooleanField(default=False)),
                ('Pizza_Sauce', models.BooleanField(default=False)),
            ],
        ),
    ]
