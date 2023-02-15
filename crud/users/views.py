from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from .forms import UserForm
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
            user = User.objects.create(
                name = form.cleaned_data.get('name'),
                last_name = form.cleaned_data.get('last_name'),
                email = form.cleaned_data.get('email'),
                active = form.cleaned_data.get('active'),
                type_user = form.cleaned_data.get('type_user'),
                photo = form.cleaned_data.get('photo')
            )
            #si es valido guardo el nuevo usuario
            user.save()
        #por ahora redirecciono a la pagina principal
        return redirect('index')

    # Si solicito la pagina de create_user
    if req.method =='GET':
        form = UserForm()
        context = {'form':form}
        return render(req,'users/create_user.html',context)


def view(req, id):
    #return HttpResponse(f'View User, id: {id}')
    user = User.objects.get(id=id)
    context = {'user':user}
    return render(req, 'users/view_user.html', context)


def edit(req, id):
    return HttpResponse(f'Edit User, id: {id}')


def delete(req, id):
    return HttpResponse(f'Delete User, id: {id}')