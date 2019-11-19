from django.contrib import admin
from .models import Music, Playlist

# Register your models here.


class MusicAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner', 'album']


class PlaylistAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Music, MusicAdmin)
admin.site.register(Playlist, PlaylistAdmin)
