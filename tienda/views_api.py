from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework import permissions,status
from rest_framework.response import Response
from .models import ProveeFruta,Fruta,Categoria
from .serializer import FraworkSerializer,FraworkSerializer2,FraworkSerializer3

# Se crea una nuevo archivo py
# que se encargará de que verifique si el administrador o usuario
# y de eso se encarga el method_decorator y el user_passes_test.
def es_administrador(user):
    ver_usuario = user.is_authenticated and user.is_staff
    return ver_usuario
# INICIO
class InicioView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
# API 1
class API1(APIView):
    permission_classes=[permissions.IsAuthenticated]
    @method_decorator(user_passes_test(es_administrador, login_url='/sin_acceso/'))
    def post(self,request,*args,**kwargs):
        informacion={
            "id": request.data.get("id"),
            "nombre": request.data.get("nombre"),
            "direccion": request.data.get("direccion"),
            "telefono": request.data.get("telefono"),
            "correo_electronico": request.data.get("correo_electronico")
        }
        serializares=FraworkSerializer(data=informacion)
        if serializares.is_valid():
            serializares.save()
            return Response(serializares.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializares.errors, status=status.HTTP_400_BAD_REQUEST)
    @method_decorator(user_passes_test(es_administrador, login_url='/sin_acceso/'))
    def get(self,request,*args,**kwargs):
        fram=ProveeFruta.objects.all()
        serializer=FraworkSerializer(fram,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
# API 2    
class API2(APIView):
    permission_classes=[permissions.IsAuthenticated]
    @method_decorator(user_passes_test(es_administrador, login_url='/sin_acceso/'))
    def post(self,request,*args,**kwargs):
        informacion={
            "id": request.data.get("id"),
            "nombre": request.data.get("nombre"),
            "tipo_fruta": request.data.get("tipo_fruta"),
            "origen": request.data.get("origen"),
            "tempo_cultivo": request.data.get("tempo_cultivo"),
            "preio": request.data.get("precio"),
            "cantidad": request.data.get("cantidad"),
            "descripcion": request.data.get("descripcion"),
            "proveedorid": request.data.get("proveedorid")
        }
        serializares=FraworkSerializer2(data=informacion)
        if serializares.is_valid():
            serializares.save()
            return Response(serializares.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializares.errors, status=status.HTTP_400_BAD_REQUEST)
    @method_decorator(user_passes_test(es_administrador, login_url='/sin_acceso/'))
    def get(self,request,*args,**kwargs):
        fram=Fruta.objects.all()
        serializer=FraworkSerializer2(fram,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
# API 2
class API3(APIView):
    permission_classes=[permissions.IsAuthenticated]
    @method_decorator(user_passes_test(es_administrador, login_url='/sin_acceso/'))
    def post(self,request,*args,**kwargs):
        informacion={
            "id": request.data.get("id"),
            "descripcion": request.data.get("descripcion"),
            "creacion": request.data.get("creacion"),
            "actualizacion": request.data.get("actualizacion"),
            "frutaid": request.data.get("frutaid")
        }
        serializares=FraworkSerializer3(data=informacion)
        if serializares.is_valid():
            serializares.save()
            return Response(serializares.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializares.errors, status=status.HTTP_400_BAD_REQUEST)
    @method_decorator(user_passes_test(es_administrador, login_url='/sin_acceso/'))
    def get(self,request,*args,**kwargs):
        fram=Categoria.objects.all()
        serializer=FraworkSerializer3(fram,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)