from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Singer(models.Model):
    name = models.CharField('Nome do Artista', max_length=250)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Artista'
        verbose_name_plural = 'Artistas'
        
class Album(models.Model):
    title = models.CharField('Nome do Album', max_length=250)
    singer = models.ForeignKey(
        Singer,
        on_delete=models.CASCADE,
        related_name='Autor'
    )
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Album'
        verbose_name_plural = 'Albuns'

class Music(models.Model):
    title = models.CharField('Título', max_length = 200)
    singer = models.ForeignKey(
        Singer,
        on_delete=models.CASCADE, 
        related_name='Autor'
    )
    album = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,
        related_name='Album'
    )
    date = models.DateField('Data de publicação')
    arq = models.FileField('Arquivo da música', blank=True, upload_to='arquivos/musicas')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Música'
        verbose_name_plural = 'Músicas'

class Playlist(models.Model):
    name = models.CharField('Nome', max_length=200)
    slug = models.SlugField('Link', max_length=200)
    music = models.ManyToManyField(Music)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        related_name='Criado'
    )
    criacao = models.DateField('Data de criação', auto_now_add=True)
    modificacao = models.DateField('Atualizado em', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Playlist'
        verbose_name_plural = 'Playlists'
