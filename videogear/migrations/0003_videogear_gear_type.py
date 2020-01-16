# Generated by Django 3.0.2 on 2020-01-15 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videogear', '0002_remove_videogear_gear_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='videogear',
            name='gear_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'headphone'), (2, 'hand mic'), (3, 'tripod'), (4, 'camera'), (5, 'tiepin mic')], default=1),
        ),
    ]
