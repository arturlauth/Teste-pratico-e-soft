from django.shortcuts import render

from cadastro.base.forms import CadastroForm


def cadastrar_pessoa(request):
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
            return sucess(request)

        else:
            print(form.errors)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CadastroForm()

    return render(request, 'base/cadastrar_pessoa.html', {'form': form})

def sucess(request):
    return render(request, 'base/sucess.html')