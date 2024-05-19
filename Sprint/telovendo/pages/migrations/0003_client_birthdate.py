import datetime
from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_client_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='birthdate',
            field=models.DateField(default=datetime.datetime(2024, 5, 8, 19, 16, 21, 973391)),
        ),
    ]
