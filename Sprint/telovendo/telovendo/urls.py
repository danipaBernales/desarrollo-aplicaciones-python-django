"""
URL configuration for telovendo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pages.views import home,list_clients,register_collab,register_client,welcome,register_admin,logout_view,a
from django.contrib.auth.views import LoginView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('clientes',list_clients),
    path('registrar_colaborador',register_collab),
    path('registrar_cliente',register_client),
    path('registrar_administrador',register_admin),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('bienvenida',welcome),
    path('logout/',logout_view),
    path("a",a)
]
