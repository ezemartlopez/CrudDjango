from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from .forms import UserForm
from django.contrib import messages
# Create your views here.
def index(req):
    users = User.objects.all()
    context = {'users':users}
    return render(req,'users/index.html',context)


def create(req):
    # Si hago un post de un nuevo usuario en create_user
    if req.method == 'POST':
        print(req.POST)
        form = UserForm(req.POST, req.FILES)
        if form.is_valid():
            #si es valido guardo el nuevo usuario
            form.save()
        #por ahora redirecciono a la pagina principal
        return redirect('index')

    # Si solicito la pagina de create_user
    if req.method =='GET':
        form = UserForm()
        url_img = '/media/images/default/no-img.png'
        context = {'form':form,'url_img':url_img}
        return render(req,'users/create_user.html',context)


def view(req, id):
    #Obtengo el usuario con ese id
    user = User.objects.get(id=id)
    #Lo agrego al contexto para que pueda ser visualizado
    context = {'user':user}
    #Envio el template que se encarga de la vista del usuario con el contexto
    return render(req, 'users/view_user.html', context)


def edit(req, id):
    #Obtengo el usuario con ese id
    user = User.objects.get(id=id)
    url_photo = user.photo.url
    if(req.method == 'GET'):
        form = UserForm(instance=user)
        context = {'form':form,'url_img':url_photo, 'id':id}
        return render(req, 'users/edit_user.html',context)
    if(req.method == 'POST'):
        form = UserForm(req.POST, req.FILES, instance=user)
        print(req.FILES)
        if(req.FILES):
            #esto podria eliminar la imagen por defecto controlo que no sea esa
            if(not(user.photo.url == 'media/images/default/no-img.png')):
                user.photo.delete()
        #Validamos que los cambios sean validos
        if form.is_valid():
            form.save()
        url_photo = User.objects.get(id=id).photo.url
        context = {'form':form,'url_img':url_photo,'id':id}
        messages.success(req,message='Contacto actualizado.', extra_tags='alert-success')
        return render(req, 'users/edit_user.html',context)


def delete(req, id):
    #Obtengo el usuario con ese id
    user = User.objects.get(id=id)
    #Elimino ese usuario, pero antes elimino la foto asociada en la carpeta media/images
    user.photo.delete()
    user.delete()
    #redirijo ala pagina principal
    return redirect('index')