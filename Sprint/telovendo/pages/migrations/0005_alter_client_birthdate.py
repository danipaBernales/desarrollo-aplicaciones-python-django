import datetime
from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_alter_client_birthdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='birthdate',
            field=models.DateField(default=datetime.datetime(2024, 5, 8, 23, 16, 58, 709212, tzinfo=datetime.timezone.utc)),
        ),
    ]
