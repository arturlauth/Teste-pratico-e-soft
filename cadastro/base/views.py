from django.shortcuts import render

from cadastro.base import facade
from cadastro.base.forms import CadastroForm


def listar_pessoa(request):
    pessoas = facade.listar_pessoas_ordenado()
    return render(request, 'sistema/listar_pessoa.html', context={'pessoas': pessoas})


def cadastrar_pessoa(request):
    initial_dict = facade.get_random_name()
    form = CadastroForm(initial=initial_dict)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CadastroForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return listar_pessoa(request)

        else:
            print(form.errors)

    return render(request, 'sistema/cadastrar_pessoa.html', {'form': form})
