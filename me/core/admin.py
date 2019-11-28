from django.contrib import admin
from .models import Music, Playlist, Artist, Album

# Register your models here.


class MusicAdmin(admin.ModelAdmin):
    list_display = ['title', 'album']
    search_fields = ['title', 'album']

class PlaylistAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'modification']
    search_fields = ['name', 'user__username']
    prepopulated_fields = {'slug' : ('name',)}


admin.site.register(Music, MusicAdmin)
admin.site.register(Playlist, PlaylistAdmin)
admin.site.register(Album)
admin.site.register(Artist)

