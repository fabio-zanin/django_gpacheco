from django.urls import path

from . import views

app_name = 'clientes'

urlpatterns = [
    path('', views.home, name='home'),    
    path('list/', views.cliente_list, name='cliente_list'),
    path('new/', views.cliente_new, name='cliente_new'),
]
