from django.urls import path

from api.views import get

urlpatterns = [
    path("towns/", get, name="get_towns"),
]
