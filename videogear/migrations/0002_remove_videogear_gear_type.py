# Generated by Django 3.0.2 on 2020-01-15 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videogear', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videogear',
            name='gear_type',
        ),
    ]