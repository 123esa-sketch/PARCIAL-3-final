from django import forms
from tienda.models import ProveeFruta
class Add_frut(forms.Form):
    nombre=forms.CharField(max_length=80)
    tipo_fruta=forms.CharField(max_length=80)
    origen=forms.CharField(max_length=70)
    tempo_cultivo=forms.DateField()
    precio=forms.FloatField()
    cantidad=forms.IntegerField()
    descripcion=forms.CharField(max_length=200)
    proveedorid=forms.ModelChoiceField(queryset=ProveeFruta.objects.all(),empty_label=None,to_field_name="id")