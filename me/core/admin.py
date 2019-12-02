from django.contrib import admin
from .models import Music, Playlist, Artist, Album

# Register your models here.
'''Arquivo que registras as classes na seção de administração do Django, permitindo que sejam geridas diretamente por lá'''

'''Classes que herdam do modelo de administrador do django, permitindo criar uma campo de busca e uma lista de informações que são previamente passadas
    na hora de apresentar as informações no administrador do Django'''
class MusicAdmin(admin.ModelAdmin):
    list_display = ['title', 'album']
    search_fields = ['title', 'album']

class PlaylistAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'modification']
    search_fields = ['name', 'user__username']
    prepopulated_fields = {'slug' : ('name',)}

class ArtistAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class AlbumAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

'''O método prepopulated_fields serve para preencher automaticamente um campo baseando-se no que é escrito em outro, nos exemplos acima está sendo passado
    as informações do campo que gera a String de cada classe para o campo Slug, que servira de atalho para as páginas específicas de cada modelo'''

'''O método register serve para de fato registrar um modelo na área de administração do Django'''
admin.site.register(Music, MusicAdmin)
admin.site.register(Playlist, PlaylistAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Artist, ArtistAdmin)

