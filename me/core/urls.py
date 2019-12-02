from django.urls import path
from . import views
'''Arquivos de URL da aplicação Core que responde requisições de URL's em branco, vindas do arquivo principal de URL do projeto: me.urls'''
urlpatterns =[
    path('', views.index, name='index'),
    path('playlist/<slug:slug>', views.playlist, name='playlist'),
    path('artista/<slug:slug>', views.artist, name='artist'),
    path('artistas', views.list_artist, name='list_artist'),
    path('album/<slug:slug>', views.album, name='album'),
]
'''As URL's que contem a sintaxe <slug:slug> estão passando o parámetro informado durante a requisição do usuário em formato de uma Slug,
ou seja, estão mandando juntamente a requisição um atalho para que seja feita uma comparação e gerada uma resposta em cima disso'''
