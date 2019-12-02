from django.shortcuts import render, get_object_or_404
from .models import Playlist, Music, Artist, Album
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

'''Arquivo que faz o Controle das requisições feitas dentro do sistema'''

'''Esse é um decoretor do Django, que gera um pedido de permissão onde apenas usuários logados podem ter acesso a tal resposta.'''
@login_required
def index(request):
    '''Método que responde ao uma requisição na página index, fazendo uma busca dentro do Banco de Dados e retornando com uma lista de
    Playlists criadas pelo usuário logado atualmente. Essas informações são passadas por um contexto para o HTML para que possam ser utilizadas lá'''
    playlist = Playlist.objects.filter(user = request.user)
    context = {
        'playlist' : playlist,
    }
    return render(request, 'index.html', context)

@login_required
def playlist(request, slug):
    '''Método que responde ao uma requisição de uma playlist, gerando uma página específica com as informações da mesma, essa requisição é baseada 
    em seu atalho (Slug). É feita uma busca dentro do Banco de Dados e tem-se como retorno uma única playlist que faça referência a Slug.
    Além disso, também é criada uma variável que contem todas as músicas da playlist, essas músicas vem de uma relação ManyToMany, e por isso são passadas
    em um objeto diferente, pois facilita sua utilização no HTML. 
    Essas informações são passadas por um contexto para o HTML para que possam ser utilizadas lá'''
    playlist = get_object_or_404(Playlist, slug=slug)
    musics = playlist.music.all()
    value = 0
    '''Aqui é feito um for para contar a quantidade de músicas que existem dentro da playlist'''
    for music in musics:
        value = value+1

    context = {
        'playlist' : playlist,
        'musics' : musics,
        'value' : value,
    }
    return render(request, 'playlist.html', context)

@login_required
def artist(request, slug):
    '''Método que responde ao uma requisição de um artista, gerando uma página específica com as informações do mesmo, essa requisição é baseada 
    em seu atalho (Slug). É feita uma busca dentro do Banco de Dados e tem-se como retorno um único artista que faça referência a Slug.
    Além disso, também é feita uma busca na classe Album para filtras todos os objetos do tipo Album que sejam de autoria do artista referenciado. 
    Essas informações são passadas por um contexto para o HTML para que possam ser utilizadas lá'''
    artist = get_object_or_404(Artist, slug=slug)
    album = Album.objects.filter(author = artist)

    context = {
        'artist' : artist,
        'album' : album, 
    }

    return render(request, 'artista.html', context)


@login_required
def album(request, slug):
    '''Método que responde ao uma requisição de um album, gerando uma página específica com as informações do mesmo, essa requisição é baseada 
    em seu atalho (Slug). É feita uma busca dentro do Banco de Dados e tem-se como retorno um único album que faça referência a Slug.
    Além disso, também é criada uma variável que contem todas as músicas do album, essas músicas vem de uma relação ManyToMany, e por isso são passadas
    em um objeto diferente, pois facilita sua utilização no HTML.
    Essas informações são passadas por um contexto para o HTML para que possam ser utilizadas lá'''
    album = get_object_or_404(Album, slug=slug)
    musics = Music.objects.filter(album = album) 
    value = 0
    '''Aqui é feito um for para contar a quantidade de músicas que existem dentro do album'''
    for music in musics:
        value = value + 1

    context = {
        'album' : album,
        'musics' : musics,
        'value' : value,
        
    }

    return render(request, 'album.html', context)


@login_required
def list_artist(request):
    '''Método que responde ao uma requisição na página artistas, fazendo uma busca dentro do Banco de Dados e retornando com uma lista contendo todos
    os artistas cadastrados no sistema. Essas informações são passadas por um contexto para o HTML para que possam ser utilizadas lá'''
    artist = Artist.objects.all()

    context = {
        'artist': artist,
    }

    return render(request, 'artistas.html', context)
