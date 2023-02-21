from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm
from django.contrib import messages
from .utilities import calculate_users_page
from django.core.paginator import Paginator

# Create your views here.
def index(req):
    #obtengo todos los usuarios
    users = User.objects.all()
    ###Seccion pagination
    #creo la paginacion indicando que quiero 5 contactos por pagina
    users_by_page = 5
    paginator = Paginator(users,users_by_page)
    page_number = req.GET.get('page')
    page_obj = paginator.get_page(page_number)
    ###Fin Seccion pagination

    #Variables para el contexto
    pages = paginator.num_pages
    list_pages = range(1, pages+1)
    total_users = len(users)
    entries_by_page = calculate_users_page(total_users,users_by_page,page_obj.number)
    #Fin variables para el contexto

    context = {'total_users': total_users,'users_by_page':entries_by_page,'page_obj': page_obj, 'pages':list_pages}
    return render(req,'users/index-v1.html',context)


def create(req):
    # Si hago un post de un nuevo usuario en create_user
    if req.method == 'POST':
        form = None
        #Si existe una imagen adjunta, utilizo un flag
        flag_img = False #hay imagen adjunta
        if req.FILES:
            form = UserForm(req.POST, req.FILES)
            flag_img = True
        else:
            form = UserForm(req.POST)
        
        if form.is_valid():
            #si es valido los campos del formulario
            if flag_img:
                #guardo el formulario con la imagen que se cargo
                form.save()
            else:
                user = User()
                #relleno los campos del usuario con el formulario
                user.name = form.cleaned_data['name']
                user.last_name = form.cleaned_data['last_name']
                user.email = form.cleaned_data['email']
                user.active = form.cleaned_data['active']
                user.type_user = form.cleaned_data['type_user']
                user.address = form.cleaned_data['address']
                user.phone = form.cleaned_data['phone']
                #guardo al usuario
                user.save()
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


def delete(req,id):
    #Obtengo el usuario con ese id
    user = User.objects.get(id=id)
    #Elimino ese usuario, pero antes elimino la foto asociada en la carpeta media/images
    #esto podria eliminar la imagen por defecto controlo que no sea esa
    if(user.photo.url != '/media/images/default/no-img.png'):
        user.photo.delete()
    user.delete()
    #redirijo ala pagina principal
    return redirect('index')