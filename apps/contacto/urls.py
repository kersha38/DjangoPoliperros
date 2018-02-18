from django.conf.urls import url, include
from apps.contacto.views import contacto_view

urlpatterns = [
    url(r'^contacto', contacto_view, name="contacto"),

]