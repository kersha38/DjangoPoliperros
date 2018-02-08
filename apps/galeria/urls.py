from django.conf.urls import url, include
from apps.galeria.views import grafico

urlpatterns = [
    url(r'^$', grafico),
    ]