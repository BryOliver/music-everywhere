from django.db import models

# Create your models here.

class Music(models.Model):
    title = models.CharField('Título', max_length = 200)
    album = models.CharField('Album', max_length=200)
    owner = models.CharField('Criador', max_length=200)
    date = models.DateField('Data de publicação')
    arq = models.FileField('Arquivo da música')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Música'
        verbose_name_plural = 'Músicas'

class Playlist(models.Model):
    slug = models.SlugField('Link', max_length=200)
    #musics = models.ManyToManyField(Music)
    name = models.CharField('Nome', max_length=200)
    blog = models.ForeignKey(Music, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Playlist'
        verbose_name_plural = 'Playlists'
