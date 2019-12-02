"""me URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core import views, urls
from users import views as users_views
from django.conf import settings
from django.conf.urls.static import static

'''Arquivos de URL da aplicação Me, a principal do sistema. Esse arquivo cuida de direcionar qual controlador deve responder as requisições feitas pelos
    usuário do sistema.'''
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('registro/',users_views.register, name = 'register'),
]

'''O django trabalha com arquivos de mídia, mas para que eles possam ser acessados dentro de nossas páginas HTML é necessário dizar para o 
    arquivo urls.py onde essas mídias podem ser encontradas, utilizando as variáveis globais MEDIA_URL e MEDIA_ROOT, definidas no arquivo de configuração 
    do projeto: settings.py'''
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
