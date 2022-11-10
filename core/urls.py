"""controle_hc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
#from django.conf.urls import url
from django.urls import path,include, re_path
from . import views
from django.contrib.auth import views as auth_views
from django.views import static as ds

from django.conf import settings
from django.conf.urls.static import static
from person import views as person
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^accounts/', include('registration.backends.simple.urls')),
    path('', views.home, name='home'),
    path('', views.home1, name='home1'),
    #path('person', person.home, name='home_map'),
    path('person/', include('person.urls')),
    path('clientes/', include('clientes.urls')),
    path('todolist/',include('todolist.urls')),
    path('blog/',include('blog.urls')),
    path('estoquevenda/', include('estoquevenda.urls')),


    re_path(r'^prestador/', include(('usuarios.urls', 'usuarios'),namespace='usuarios')),
    re_path(r'^prestador/', include(('prestadores.urls','prestadores'),namespace='prestadores')),
    re_path(r'^select2/', include('django_select2.urls')),
     

    re_path(r'^media/(?P<path>.*)$', ds.serve,
            {'document_root': settings.MEDIA_ROOT, }, name="media"),
  
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
