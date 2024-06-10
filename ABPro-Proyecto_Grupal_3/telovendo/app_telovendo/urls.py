from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.customer_list, name='customer_list'),
]