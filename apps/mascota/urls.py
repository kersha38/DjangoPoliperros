from django.conf.urls import url
from apps.mascota.views import index, mascota_crear, mascota_list, mascota_edit, mascota_delete

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo', mascota_crear, name='mascotaCrear'),
    url(r'^listar/', mascota_list, name='mascotaListar'),
    url(r'^editar/(?P<id_mascota>\d+)/$', mascota_edit, name='mascotaEditar'),
    url(r'^eliminar/(?P<id_mascota>\d+)/$', mascota_delete, name='mascotaEliminar'),
]