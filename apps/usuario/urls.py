from django.conf.urls import url
from apps.usuario.views import RegistroUsuario, principal
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^registrar', RegistroUsuario.as_view(), name="registrarUsu"),
    url(r'^$', principal),

]