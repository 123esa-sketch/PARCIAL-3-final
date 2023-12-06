from rest_framework import serializers
from .models import ProveeFruta,Fruta,Categoria

class FraworkSerializer(serializers.ModelSerializer):
        class Meta:
            model=ProveeFruta
            fields = ["id","nombre","direccion","telefono","correo_electronico"]

class FraworkSerializer2(serializers.ModelSerializer):
        class Meta:
            model=Fruta
            fields = ["id","nombre","tipo_fruta","origen","tempo_cultivo","precio","cantidad","descripcion","proveedorid"]

class FraworkSerializer3(serializers.ModelSerializer):
        class Meta:
            model=Categoria
            fields = ["id","descripcion","creacion","actualizacion","frutaid"]