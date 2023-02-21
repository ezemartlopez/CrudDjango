from django.forms import ModelForm,FileInput, TextInput, EmailInput, DateInput,CheckboxInput,Select
from .models import User, USER_TYPE

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'name':TextInput(attrs={'type':'text','placeholder':'Ingrese los Nombres', 'class':'form-control'}),
            'last_name':TextInput(attrs={'type':'text','placeholder':'Ingrese los Apellidos', 'class':'form-control'}),
            'email':EmailInput(attrs={'type':'text','placeholder':'Ingrese el Email', 'class':'form-control'}),
            'active':CheckboxInput(attrs={'type':'checkbox','class':'checkbox'}),
            'type_user':Select(attrs={'type':'select', 'class':'form-control'},choices=USER_TYPE),
            'photo':FileInput(attrs={'type':'file','id':'seleccionArchivos','class':'form-control'}),
            'date_created':DateInput(attrs={'type':'date'}),
            'address':TextInput(attrs={'type':'text','placeholder':'Ingrese su direccion', 'class':'form-control'}),
            'phone':TextInput(attrs={'type':'text','placeholder':'Ingrese su telefono', 'class':'form-control'})
        }