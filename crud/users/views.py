from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(req):
    return HttpResponse('Index')

def create(req):
    return HttpResponse('Create User')

def view(req, id):
    return HttpResponse('View User')

def edit(req, id):
    return HttpResponse('Edit User')

def delete(req, id):
    return HttpResponse('Delete User')