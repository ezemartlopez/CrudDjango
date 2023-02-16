from django.forms import ModelForm,FileInput, TextInput, EmailInput, DateInput,CheckboxInput,Select
from .models import User, USER_TYPE

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'name':TextInput(attrs={'type':'text','placeholder':'Nombres', 'class':'form-control'}),
            'last_name':TextInput(attrs={'type':'text','placeholder':'Apellidos', 'class':'form-control'}),
            'email':EmailInput(attrs={'type':'text','placeholder':'Email', 'class':'form-control'}),
            'active':CheckboxInput(attrs={'type':'checkbox', 'class':'form-check-input'}),
            'type_user':Select(attrs={'type':'select', 'class':'form-select'},choices=USER_TYPE),
            'photo':FileInput(attrs={'type':'file','placeholder':'Foto o Imagen','class':'form-control'}),
            'date_created':DateInput(attrs={'type':'date'})


        }