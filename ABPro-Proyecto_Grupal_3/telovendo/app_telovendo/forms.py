from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'last_name', 'email', 'birth_city', 'address', 'phone_number', 'creation_date']