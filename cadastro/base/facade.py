import requests


def get_random_name():
    response = requests.get('https://gerador-nomes.herokuapp.com/nomes/2')
    key_list = ['nome', 'sobrenome']
    name_list = response.json()
    name_dictionary = dict(zip(key_list, name_list))
    return name_dictionary
