from django.contrib import admin
from .models import Music, Playlist

# Register your models here.


class MusicAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner', 'album']

admin.site.register(Music, MusicAdmin)
admin.site.register(Playlist)
