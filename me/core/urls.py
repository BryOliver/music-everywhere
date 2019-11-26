from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name='index'),
    path('playlist/<slug:slug>', views.playlist, name='playlist'),
]
