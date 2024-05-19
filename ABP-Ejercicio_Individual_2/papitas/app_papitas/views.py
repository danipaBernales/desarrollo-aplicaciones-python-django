from django.shortcuts import render
from django.http import HttpResponse

def my_view(request):
    return render(request, 'app_papitas/templates/index.html')
