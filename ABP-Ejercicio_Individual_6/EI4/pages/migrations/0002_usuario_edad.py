# Generated by Django 5.0.4 on 2024-04-20 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='edad',
            field=models.IntegerField(default=12),
        ),
    ]
