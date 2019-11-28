from django.shortcuts import render, get_object_or_404
from .models import Playlist, Music
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
