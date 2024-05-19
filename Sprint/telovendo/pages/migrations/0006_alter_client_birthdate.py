import django.utils.timezone
from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_alter_client_birthdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='birthdate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
