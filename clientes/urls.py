from django.urls import path

from . import views

app_name = 'clientes'

urlpatterns = [
    path('list/', views.cliente_list, name='cliente_list'),
    path('new/', views.cliente_new, name='cliente_new'),
    path('update/<int:id>/', views.cliente_update, name='cliente_update'),
    path('delete/<int:id>/', views.cliente_delete, name='cliente_delete'),
]
