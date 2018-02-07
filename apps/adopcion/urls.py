from django.conf.urls import url
from apps.adopcion.views import index, SolicitudList, SolicitudCreate\
    ,solicitudDelete,SolicitudUpdate

urlpatterns = [
    url(r'^$', index),
    url(r'^solicitud/listar/$', SolicitudList.as_view(), name='solicitudList'),
    url(r'^solicitud/nueva/$', SolicitudCreate.as_view(), name='solicitudCrear'),
    url(r'^solicitud/borrar/(?P<pk>\d+)/$', solicitudDelete.as_view(), name='solicitudBorrar'),
    url(r'^solicitud/editar/(?P<pk>\d+)/$', SolicitudUpdate.as_view(), name='solicitudEdit'),
]