from django.shortcuts import render, get_object_or_404
from .models import Playlist, Music, Artist, Album
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    playlist = Playlist.objects.filter(user = request.user)
    context = {
        'playlist' : playlist,
    }
    return render(request, 'index.html', context)

@login_required
def playlist(request, slug):
    playlist = get_object_or_404(Playlist, slug=slug)
    musics = playlist.music.all()
    value = 0
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
    artist = get_object_or_404(Artist, slug=slug)
    album = Album.objects.filter(author = artist)

    context = {
        'artist' : artist,
        'album' : album, 
    }

    return render(request, 'artista.html', context)


@login_required
def album(request, slug):
    album = get_object_or_404(Album, slug=slug)
    musics = Music.objects.filter(album = album) 
    value = 0
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
    artist = Artist.objects.all()

    context = {
        'artist': artist,
    }

    return render(request, 'artistas.html', context)
