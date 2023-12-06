from django import forms

class Categoria(forms.Form):
    descripcion=forms.CharField(max_length=200)
    creacion=forms.DateField()
    actualizacion=forms.DateField()
    frutaid=forms.IntegerField()
