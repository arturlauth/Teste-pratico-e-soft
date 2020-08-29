from django.urls import path

from cadastro.base import views

urlpatterns = [
    path('cadastrar', views.index, name='index'),
]
