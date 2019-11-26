# music-everywhere
Repositório para a cadeira de Programação Orientada a Objetos, UFRN.
Um pequeno sistema para guardar músicas.

# Instruções de uso
Recomendo a criação de um ambiente virtual para instalar as dependencias corretas do projeto. 

- Criar ambiente virtual (https://pythonacademy.com.br/blog/python-e-virtualenv-como-programar-em-ambientes-virtuais)
- Após a criação, deve-se entrar no ambiente e instalar os pacotes necessários para executar o projeto
- Para instalar os pacotes execute: pip install -r requirements.txt
- Após a instalação basta executar o servidor local: python manage.py makemigrations
- Em seguida o comando python manage.py migrate (os comandos servem para sincronizar o Banco de Dados)
- Para rodar o servidor local: python manage.py runserver

# URLS do projeto
- localhost: página principal
- localhost/login: página de login
- localhost/registro: página de registro para novo usuário
- localhost/admin: área de administração do site (usuário: admin; senha: poo@2019)
- localhost/playlist/nome-da-playlist: página contendo as músicas da playlist