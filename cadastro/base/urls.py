from django.urls import path

from cadastro.base import views

urlpatterns = [
    path('cadastrar', views.cadastro_pessoa, name='cadastro_pessoa')
]
