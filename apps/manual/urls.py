from django.conf.urls import url, include
from apps.manual.views import manual

urlpatterns = [
    url(r'^$', manual, name="quienes"),
    ]