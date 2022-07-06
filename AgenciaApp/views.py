from django.http import HttpResponse
from django.shortcuts import render
from .models import Auto
from .forms import BusquedaAuto, FormularioAuto

# Create your views here.


def index(request):

    return render(request, "base.html")


def crear_auto(request):
    if request.method == "POST":
        formulario_auto = FormularioAuto(request.POST)
        print(formulario_auto)

        if formulario_auto.is_valid:
            informacion = formulario_auto.cleaned_data
            auto = Auto(
                marca=informacion["marca"],
                color=informacion["color"],
                modelo=informacion["modelo"],
            )
            auto.save()

            return render(request, "crear_auto.html")

    else:
        formulario_auto = FormularioAuto()

    return render(request, "crear_auto.html", {"form": formulario_auto})


def buscar_auto(request):

    marca_de_busqueda = request.GET.get("marca")

    if marca_de_busqueda:
        listado_autos = Auto.objects.filter(marca__icontains=marca_de_busqueda)
    else:
        listado_autos = Auto.objects.all()

    form = BusquedaAuto()
    return render(
        request, "buscar_auto.html", {"listado_autos": listado_autos, "form": form}
    )


def sobre_nosotros(request):
    return render(request, "sobre_nosotros.html")
