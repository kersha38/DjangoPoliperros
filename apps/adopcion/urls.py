from django.conf.urls import url
from apps.adopcion.views import index, SolicitudList, SolicitudCreate\
    ,solicitudDelete,SolicitudUpdate,atenderSolicitud
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', index),
    url(r'^solicitud/listar/$', login_required(SolicitudList.as_view()), name='solicitudList'),
    url(r'^solicitud/nueva/$', SolicitudCreate.as_view(), name='solicitudCrear'),
    url(r'^solicitud/borrar/(?P<pk>\d+)/$', login_required( solicitudDelete.as_view()), name='solicitudBorrar'),
    url(r'^solicitud/editar/(?P<pk>\d+)/$',  login_required(SolicitudUpdate.as_view()), name='solicitudEdit'),
    url(r'^solicitud/atender/(?P<pk>\d+)/$', login_required( atenderSolicitud), name='solicitudAtender'),
]