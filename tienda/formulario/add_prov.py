from django import forms

class Add_provf(forms.Form):
    nombre=forms.CharField(max_length=80)
    direccion=forms.CharField(max_length=200)
    telefono=forms.CharField(max_length=12)
    correo_electronico=forms.EmailField()