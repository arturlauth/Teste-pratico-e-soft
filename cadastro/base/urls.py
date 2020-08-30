from django.urls import path

from cadastro.base import views

app_name = 'base'
urlpatterns = [
    path('cadastrar_pessoa/', views.cadastrar_pessoa, name='cadastrar_pessoa'),
    path('listar_pessoa/', views.listar_pessoa, name='listar_pessoa'),
]
