from django.db import models
from django.contrib.auth.models import User
from django_currentuser.db.models import CurrentUserField

# Create your models here.
'''Arquivo de Modelos, onde ficaram guardadas as classes do sistema ME!'''
class Artist(models.Model):
    '''Modelo da classe artista, contendo um campo de nome, biografia, um campo para seleção de imagem 
    e um campo de atalho que é preenchido automaticamente'''

    name = models.CharField('Nome do Artista', max_length=250)
    slug = models.SlugField('Atalho', max_length=200)
    biography = models.TextField('Biografia')
    image = models.ImageField(
        verbose_name='Imagem do artista', 
        upload_to='arquivos/imagens/artistas'
    )
    
    '''Método da classe Artist que gera uma URL baseada em seu campo de atalho
    Tal URL será utilizada para acessar uma página específica contendo as informações de um único artista'''
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('artist', args=[self.slug])
    
    '''Método que define como será a representação de uma string da classe Artist'''
    def __str__(self):
        return self.name

    '''Classe que acessa as configurações do Django e modifica a parte de administrador, utilizando nomes mais estilizados'''
    class Meta:
        verbose_name = 'Artista'
        verbose_name_plural = 'Artistas'
        
class Album(models.Model):
    '''Modelo da classe Album, contendo um campo de título, um campo de atalho, um campo de imagem, um campo para data de publicação 
    e uma relação Muitos Para Muitos com a classe Artist'''
    title = models.CharField('Nome do Album', max_length=250)
    slug = models.SlugField('Atalho', max_length=200)
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

    '''Método da classe Album que gera uma URL baseada em seu campo de atalho
    Tal URL será utilizada para acessar uma página específica contendo as informações de um único album'''
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('album', args=[self.slug])

    '''Método que define como será a representação de uma string da classe Album'''
    def __str__(self):
        return self.title

    '''Classe que acessa as configurações do Django e modifica a parte de administrador, utilizando nomes mais estilizados'''
    class Meta:
        verbose_name = 'Album'
        verbose_name_plural = 'Albuns'

class Music(models.Model):
    '''Modelo da classe Music, contendo um campo de título, um campo para a duração da música, um campo para a sua data de publicação, 
    um campo para selecionar o arquivo da música, uma relação Muitos para Muitos com a classe Artist e uma relação de chave estrangeira,
    Um para Um, com a classe Album'''
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

    '''Método que define como será a representação de uma string da classe Music'''
    def __str__(self):
        return self.title

    '''Classe que acessa as configurações do Django e modifica a parte de administrador, utilizando nomes mais estilizados'''
    class Meta:
        verbose_name = 'Música'
        verbose_name_plural = 'Músicas'

class Playlist(models.Model):
    '''Modelo da classe Playlist, contendo um campo para o nome, atalho, imagem, data de criação, data de modificação
    uma relação Muitos para Muitos com a classe Música e com a classe usuários, que mostra os contribuidores da Playlist, e uma relação especial
    com o usuário logado atualmente'''
    name = models.CharField('Nome', max_length=200)
    slug = models.SlugField('Atalho', max_length=200)
    music = models.ManyToManyField(Music, verbose_name='Lista de Músicas')
    contributors = models.ManyToManyField(User, verbose_name='Colaboradores', related_name='colaboradores', null=True, blank=True)
    image = models.ImageField(
        verbose_name='Imagem da playlist',
        upload_to='arquivos/imagens/playlist',
        null=True
    )
    '''O campo CurrentUser é uma aplicação externa que permite selecionar automaticamento o usuário logado e atribuir seu valor ao campo'''
    user = CurrentUserField(verbose_name='Criador', related_name='user')
    creation = models.DateField('Data de criação', auto_now_add=True)
    modification = models.DateField('Atualizado em', auto_now=True)

    '''Método que define como será a representação de uma string da classe Playlist'''
    def __str__(self):
        return self.name

    '''Método da classe Playlist que gera uma URL baseada em seu campo de atalho
    Tal URL será utilizada para acessar uma página específica contendo as informações de uma única playlist'''
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('playlist', args=[self.slug])

    '''Classe que acessa as configurações do Django e modifica a parte de administrador, utilizando nomes mais estilizados'''
    class Meta:
        verbose_name = 'Playlist'
        verbose_name_plural = 'Playlists'
