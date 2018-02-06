from django.conf.urls import url
from apps.mascota.views import index, mascota_crear, mascota_list, mascota_edit

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo', mascota_crear, name='mascota_crear'),
    url(r'^listar/', mascota_list, name='mascota_listar'),
    url(r'^editar/(?P<id_mascota>\d+)/$', mascota_edit, name='mascota_editar'),
]