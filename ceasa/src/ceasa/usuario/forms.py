from django import forms
from escola.models import Escola
import hashlib

# Create your form here.
class UsuarioForm(forms.Form):
	nome 		=	forms.CharField(label='Nome', max_length=100)
	cpf 		=	forms.CharField(label='CPF', max_length=14)
	email 		=	forms.EmailField(label='Email', max_length=45)
	telefone 	=	forms.CharField(label='Telefone', max_length=15)
	senha 		=	forms.CharField(label='Senha', max_length=100, widget=forms.PasswordInput)
	tipo 		=	forms.CharField(label='Tipo', max_length=1)
	escola		=	forms.ModelChoiceField(label='Escola', widget=forms.Select, queryset=Escola.objects.all(), required=False)

	def clean_form(self):
		nome 		=	self.cleaned_data.get('nome')
		cpf			= 	self.cleaned_data.get('cpf')
		email 		=	self.cleaned_data.get('email')
		telefone	=	self.cleaned_data.get('telefone')
		senha		=	self.cleaned_data.get('senha')
		tipo 		=	self.cleaned_data.get('tipo')
		escola 		=	self.cleaned_data.get('escola')

		senha_hash = hashlib.sha256(senha.encode()).hexdigest()
		
		return {
			'nome': nome,
			'cpf': cpf,
			'email': email,
			'telefone': telefone,
			'senha': senha_hash,
			'tipo': tipo,
			'escola': escola,
		}

class UsuarioEditarForm(forms.Form):
	nome 		=	forms.CharField(label='Nome', max_length=100)
	cpf 		=	forms.CharField(label='CPF', max_length=14)
	email 		=	forms.EmailField(label='Email', max_length=45)
	telefone 	=	forms.CharField(label='Telefone', max_length=15)
	senha 		=	forms.CharField(label='Senha', max_length=100, widget=forms.PasswordInput, required=False)
	tipo 		=	forms.CharField(label='Tipo', max_length=1)
	escola		=	forms.ModelChoiceField(label='Escola', widget=forms.Select, queryset=Escola.objects.all(), required=False)

	def clean_form(self):
		nome 		=	self.cleaned_data.get('nome')
		cpf			= 	self.cleaned_data.get('cpf')
		email 		=	self.cleaned_data.get('email')
		telefone	=	self.cleaned_data.get('telefone')
		senha		=	self.cleaned_data.get('senha')
		tipo 		=	self.cleaned_data.get('tipo')
		escola 		=	self.cleaned_data.get('escola')

		senha_hash = hashlib.sha256(senha.encode()).hexdigest()
		
		return {
			'nome': nome,
			'cpf': cpf,
			'email': email,
			'telefone': telefone,
			'senha': senha_hash,
			'tipo': tipo,
			'escola': escola,
		}