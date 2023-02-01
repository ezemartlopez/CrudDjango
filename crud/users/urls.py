from django.urls import path
from . import views
urlpatterns = [
    path('', view=views.index, name='index'),
    path('create/',view=views.create, name='user_create'),
    path('view/<int:id>',view=views.view, name='user_view'),
    path('edit/<int:id>',view=views.edit, name='user_edit'),
    path('delete/<int:id>',view=views.delete, name='user_delete')
]
