from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(req):
    return render(req,'users/index.html',{})

def create(req):
    return HttpResponse('Create User')

def view(req, id):
    return HttpResponse(f'View User, id: {id}')

def edit(req, id):
    return HttpResponse(f'Edit User, id: {id}')

def delete(req, id):
    return HttpResponse(f'Delete User, id: {id}')