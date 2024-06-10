from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Customer
from .forms import CustomerForm

def home(request):
    return render(request,'index.html')

def customer_list(request):
    customers = Customer.objects.all()[:5]
    return render(request, 'customer_list.html', {'customers': customers})