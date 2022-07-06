from django.urls import path
from .views import index, crear_auto, buscar_auto, sobre_nosotros

urlpatterns = [
    path("", index, name="index"),
    path("crearauto/", crear_auto, name="crear_auto"),
    path("buscarauto/", buscar_auto, name="buscar_auto"),
    path("sobrenosotros/", sobre_nosotros, name="sobre_nosotros"),
]
