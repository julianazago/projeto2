from django import forms
from usuario.models import Usuario


class UsuarioForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Usuario
        
class LoginForm(forms.Form):
    login = forms.CharField(max_length=100, required=True)
    senha = forms.CharField(widget=forms.PasswordInput, required=True)

class cadastroForm(forms.Form):
    login = forms.CharField(max_length=100, required=True)
    senha = forms.CharField(widget=forms.PasswordInput, required=True)
    email = forms.CharField(max_length=100, required=True)
    
class CorridaForm(forms.Form):
    enderecoBusca = forms.CharField(max_length=100, required=True)
    enderecoLeva = forms.CharField(max_length=100, required=True)
    clienteNome = forms.CharField(max_length=100, required=True)
   
