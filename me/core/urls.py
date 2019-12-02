from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name='index'),
    path('playlist/<slug:slug>', views.playlist, name='playlist'),
    path('artista/<slug:slug>', views.artist, name='artist'),
    path('artistas', views.list_artist, name='list_artist'),
    path('album/<slug:slug>', views.album, name='album'),
]
