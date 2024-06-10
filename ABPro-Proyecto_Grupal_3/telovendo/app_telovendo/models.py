from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    email = models.EmailField()
    birth_city = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} {self.last_name}'
