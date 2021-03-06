from django.conf.urls import url
from apps.mascota.views import index, mascota_crear, mascota_list, mascota_edit, mascota_delete, \
    MascotaList, MascotaCreate, MascotaUpdate, MascotaDelete

urlpatterns = [
    url(r'^$', index, name='index'),
    #url(r'^nuevo/$', mascota_crear, name='mascotaCrear'), #mediante funcion
    url(r'^nuevo/$', MascotaCreate.as_view(), name='mascotaCrear'), #mediante clases
    #url(r'^listar/$', mascota_list, name='mascotaListar'), #mediante funcion
    url(r'^listar/$', MascotaList.as_view(), name='mascotaListar'), #mediante clase
    #url(r'^editar/(?P<id_mascota>\d+)/$', mascota_edit, name='mascotaEditar'),
    url(r'^editar/(?P<pk>\d+)/$', MascotaUpdate.as_view(), name='mascotaEditar'),
    #url(r'^eliminar/(?P<id_mascota>\d+)/$', mascota_delete, name='mascotaEliminar'),
    url(r'^eliminar/(?P<pk>\d+)/$', MascotaDelete.as_view(), name='mascotaEliminar'),
]