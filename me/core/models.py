from django.db import models
from django.contrib.auth.models import User
from django_currentuser.db.models import CurrentUserField

# Create your models here.
class Artist(models.Model):
    name = models.CharField('Nome do Artista', max_length=250)
    biography = models.TextField('Biografia')
    image = models.ImageField(
        verbose_name='Imagem do artista', 
        upload_to='arquivos/imagens/artistas'
    )
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Artista'
        verbose_name_plural = 'Artistas'
        
class Album(models.Model):
    title = models.CharField('Nome do Album', max_length=250)
    image = models.ImageField(
        verbose_name='Imagem do album',
        upload_to='arquivos/imagens/album',
        null=True
    )
    author = models.ManyToManyField(
        Artist,
        verbose_name='Artistas'
    )
    release = models.DateField('Data de publicação', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Album'
        verbose_name_plural = 'Albuns'

class Music(models.Model):
    title = models.CharField('Título', max_length = 200)
    artist = models.ManyToManyField(
        Artist,
        related_name='artist',
        verbose_name='Artista'
    )
    album = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,
        related_name='music_album',
        verbose_name='Album'
    )
    duration = models.DurationField('Duração da Música', null=True)
    date = models.DateField('Data de publicação')
    file = models.FileField('Arquivo da música', blank=True, upload_to='arquivos/musicas')

    # def save(self, force_update=False, force_insert=False):
    #     alb = self.album
    #     singer_album = Album.objects.get(title = alb)
    #     self.singer = singer_album.singer
    #     super().save(force_insert, force_update)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Música'
        verbose_name_plural = 'Músicas'

class Playlist(models.Model):
    name = models.CharField('Nome', max_length=200)
    slug = models.SlugField('Atalho', max_length=200)
    music = models.ManyToManyField(Music, verbose_name='Lista de Músicas')
    contributors = models.ManyToManyField(User, verbose_name='Colaboradores', related_name='colaboradores', null=True, blank=True)
    image = models.ImageField(
        verbose_name='Imagem da playlist',
        upload_to='arquivos/imagens/playlist',
        null=True
    )
    user = CurrentUserField(verbose_name='Criador', related_name='user')
    creation = models.DateField('Data de criação', auto_now_add=True)
    modification = models.DateField('Atualizado em', auto_now=True)
    image = models.ImageField(
        verbose_name='Imagem da playlist',
        upload_to='arquivos/imagens/playlist',
        null=True
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('playlist', args=[self.slug])

    class Meta:
        verbose_name = 'Playlist'
        verbose_name_plural = 'Playlists'
