from django.urls import path

from cadastro.base import views

app_name = 'base'
urlpatterns = [
    path('cadastrar_pessoa/', views.cadastrar_pessoa, name='cadastrar_pessoa'),
    path('base/', views.base, name='base'),
    path('listar_pessoa/', views.listar_pessoa, name='listar_pessoa')
]
