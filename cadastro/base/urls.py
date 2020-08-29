from django.urls import path

from cadastro.base import views

urlpatterns = [
    path('cadastrar_pessoa/', views.cadastrar_pessoa, name='cadastrar_pessoa'),
    path('sucess/', views.sucess, name='sucess')
]
