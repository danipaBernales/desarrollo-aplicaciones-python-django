# Generated by Django 5.0.4 on 2024-04-26 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_alter_client_options_alter_client_managers_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='total_spend',
            field=models.IntegerField(default=0),
        ),
    ]
