from typing import List

import requests

from cadastro.base.models import Pessoa


def get_random_name():
    response = requests.get('https://gerador-nomes.herokuapp.com/nomes/2')
    key_list = ['nome', 'sobrenome']
    name_list = response.json()
    name_dictionary = dict(zip(key_list, name_list))
    return name_dictionary


def listar_pessoas_ordenado() -> List[Pessoa]:
    return list(Pessoa.objects.order_by('nome').all())
