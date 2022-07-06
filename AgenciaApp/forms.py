from django import forms


class FormularioAuto(forms.Form):
    marca = forms.CharField(max_length=30)
    color = forms.CharField(max_length=30)
    modelo = forms.IntegerField()


class BusquedaAuto(forms.Form):
    marca = forms.CharField(max_length=30, required=False)
