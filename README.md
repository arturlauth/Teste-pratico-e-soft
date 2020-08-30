# Teste-pratico-e-soft
[![Build Status](https://travis-ci.com/arturlauth/Teste-pratico-e-soft.svg?branch=master)](https://travis-ci.com/arturlauth/Teste-pratico-e-soft)

Projeto em Django - Resolução do teste prático para processo seletivo e-soft sistemas 

# Modo de Usar:

Basta baixar o repositório, usar o pipenv update para instalação das dependências necessárias para funcionamento do sistema.
Feito isso rodar o comando mng runserver no terminal e abrir em seu navegador o endereço que aparecer na tela.

# Página cadastrar: 

Preencha o formulário e clique no botão criar pessoa. Os dados serão salvos no banco de dados (arquivo db.sqlite3), para escalabilidade seria recomendado usar outro banco de dados, eu optaria pelo postgreSQL.

# Página Listar:

Lista, em ordem alfabética, todas pessoas cadastradas no sistema.

# Página Editar:

Foi criado um usuário no admin do django com permissão para excluir, editar, adicionar Pessoa. 
Login: admin@admin.com 
Senha: adm304050
