from django.urls import path,include, re_path
from . import views
from django.views import static as ds
from django.conf import settings
from django.conf.urls.static import static

app_name = 'person'

urlpatterns = [
    path('', views.homeperson, name='home_map'),
    path('person/sucesso', views.sucesso3, name='sucesso'),
    path('person/<int:id>', views.homeperson, name='homeperson'),

    re_path(r'^media/(?P<path>.*)$', ds.serve,
            {'document_root': settings.MEDIA_ROOT, }, name="media"),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
