from django.db import models

# Create your models here.

class Music(models.Model):
    title = models.CharField('Título', max_length = 200)
    album = models.CharField('Album', max_length=200)
    owner = models.CharField('Criador', max_length=200)
    date = models.DateField('Data de publicação')
    arq = models.FileField('Arquivo da música')

    def __str__():
        return self.title

    class Meta:
        verbose_name = 'Música'
        verbose_name_plural = 'Músicas'

class Playlist(models.Model):
    pass 