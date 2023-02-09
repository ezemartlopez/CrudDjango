from django.shortcuts import render
from django.http import HttpResponse
from .models import User

# Create your views here.
def index(req):
    users = User.objects.all()
    context = {'users':users}
    return render(req,'users/index.html',context)

def create(req):
    return HttpResponse('Create User')

def view(req, id):
    #return HttpResponse(f'View User, id: {id}')
    user = User.objects.get(id=id)
    context = {'user':user}
    return render(req, 'users/view_user.html', context)

def edit(req, id):
    return HttpResponse(f'Edit User, id: {id}')

def delete(req, id):
    return HttpResponse(f'Delete User, id: {id}')