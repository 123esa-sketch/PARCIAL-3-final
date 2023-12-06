from django.shortcuts import render,redirect,get_object_or_404
from .formulario.registroform import NewUserForm
from .formulario.loginform import LoginForm
from .formulario import add_cat as fm
from .formulario import add_frut as fm1
from .formulario import add_prov as fm3
from django.http import HttpResponseRedirect
from .models import ProveeFruta,Fruta,Categoria
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required,user_passes_test

# Registor de usuario
def reg_user(request):
    if request.method == "POST":
        formulario=NewUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
        return HttpResponseRedirect("/")
    else:
        formulario=NewUserForm()
        return render(request,"Reg_user.html",{"form":formulario})
# Index principal
def index(request):
    return render(request, 'index.html')

# Si es administrador mostramos en terminal
def es_administrador(user):
    ver_usuario = user.is_authenticated and user.is_staff
    print(f"Usuario: {user.username}, ¿Es administrador?: {ver_usuario}")
    return ver_usuario

# Función para iniciar sesión
def iniciar_sesion(request):
    if request.method=='POST':
        form=LoginForm(request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
    else:
        form=LoginForm()
    return render(request,'login.html',{'form':form})

# Cerrar sesión
def cerrar_sesion(request):
    logout(request)
    return redirect('login')

#accede al index al iniciar sesi+on
@login_required(login_url=login)
def index(request):
    return render(request,'index.html',{'user':request.user})

# dependiendo si es administrador o usuario común tendrá acceso al index pero
# solo observará
@login_required(login_url='login')
def index(request):
    es_estudiante=request.user.groups.filter(name='Estudiante').exists()
    es_admin=request.user.is_staff
    if es_estudiante or es_admin:
        return render(request,'index.html',{'user':request.user,'es_estudiante':es_estudiante,'es_admin':es_admin})
    else:
        return render(request,'index.html')

# Lista de proveedores de frutas se utliza el user_passes_test y el es_administrador
# cuando se registra si es admin tendrá acceso a la tabla de provfruta.
@user_passes_test(es_administrador,login_url='/sin_acceso/')
def list_provf(request):
    proveedores = ProveeFruta.objects.all()
    return render(request, "lisprovf.html",{'lisprovf':proveedores})


# función no acceso
def sin_acceso(request):
    return render(request, 'sin_acceso.html')

# Añadirá proveedor solo si es administrador 
@user_passes_test(es_administrador,login_url='/sin_acceso/')
def add_provf(request):
    if request.method == "POST":
        formulario = fm3.Add_provf(request.POST)
        if formulario.is_valid():
            nuepr=ProveeFruta()
            nuepr.nombre=formulario.cleaned_data["nombre"] 
            nuepr.direccion=formulario.cleaned_data["direccion"] 
            nuepr.telefono=formulario.cleaned_data["telefono"]
            nuepr.correo_electronico=formulario.cleaned_data["correo_electronico"]
            nuepr.save()
            return HttpResponseRedirect("/")
    else:
        formulario=fm3.Add_provf()
    usuario_actual=request.user
    es_admin=usuario_actual.is_authenticated and usuario_actual.is_staff
    return render(request, "Add_provf.html",{"form":formulario, "es_admin":es_admin})

# Observará la lista de fruta si es administrador
@user_passes_test(es_administrador,login_url='/sin_acceso/')
def list_frut(request):
    frutas = Fruta.objects.all()
    return render(request, "lisfrut.html",{'lisfrut':frutas})

# Añadirá fruta solo si es administrador
@user_passes_test(es_administrador,login_url='/sin_acceso/')
def add_frut(request):
    if request.method == "POST":
        formulario = fm1.Add_frut(request.POST)
        if formulario.is_valid():
            nuefru=Fruta()
            nuefru.nombre=formulario.cleaned_data["nombre"]
            nuefru.tipo_fruta=formulario.cleaned_data["tipo_fruta"]
            nuefru.origen=formulario.cleaned_data["origen"]
            nuefru.tempo_cultivo=formulario.cleaned_data["tempo_cultivo"]
            nuefru.precio=formulario.cleaned_data["precio"]
            nuefru.cantidad=formulario.cleaned_data["cantidad"]
            nuefru.descripcion=formulario.cleaned_data["descripcion"]
            proveedorid=formulario.cleaned_data["proveedorid"]
            nuefru.proveedorid=proveedorid
            nuefru.save()
            return HttpResponseRedirect("/")
    else:
        formulario=fm1.Add_frut()
    usuario_actual=request.user
    es_admin=usuario_actual.is_authenticated and usuario_actual.is_staff
    return render(request, "Add_frut.html",{"form":formulario, "es_admin":es_admin})

# Observará la lista de cat si es administrador si no lo mandará al html sin_acceso.
@user_passes_test(es_administrador,login_url='/sin_acceso/')
def list_cat(request):
    categorias = Categoria.objects.all()
    return render(request, "liscat.html",{'liscat':categorias})

# Añadirá una categoría si es administrador
@user_passes_test(es_administrador,login_url='/sin_acceso/')
def add_cat(request):
    if request.method == "POST":
        formulario = fm.Categoria(request.POST)
        if formulario.is_valid():
            nuecat=Categoria()
            nuecat.descripcion=formulario.cleaned_data["descripcion"]
            nuecat.creacion=formulario.cleaned_data["creacion"]
            nuecat.actualizacion=formulario.cleaned_data["actualizacion"]
            frutaid=formulario.cleaned_data["frutaid"]
            nuecat.frutaid=get_object_or_404(Fruta,id=frutaid)
            nuecat.save()
            return HttpResponseRedirect("/")
    else:
        formulario=fm.Categoria()
    usuario_actual=request.user
    es_admin=usuario_actual.is_authenticated and usuario_actual.is_staff
    return render(request, "Add_cat.html",{"form":formulario, "es_admin":es_admin})
