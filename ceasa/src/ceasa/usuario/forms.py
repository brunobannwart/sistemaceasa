from django import forms
import hashlib

# Create your form here.
class UsuarioForm(forms.Form):
	nome 		=	forms.CharField(label='Nome', max_length=100)
	cpf 		=	forms.CharField(label='Nome', max_length=14)
	telefone 	=	forms.CharField(label='Nome', max_length=15)
	senha 		=	forms.CharField(label='Nome', max_length=100, widget=forms.PasswordInput)
	tipo 		=	forms.CharField(label='Nome', max_length=1)

	def clean_form(self):
		nome 		=	self.cleaned_data.get('nome')
		cpf			= 	self.cleaned_data.get('cpf')
		telefone	=	self.cleaned_data.get('telefone')
		senha		=	self.cleaned_data.get('senha')
		tipo 		=	self.cleaned_data.get('tipo')

		senha_hash = hashlib.sha256(senha.encode()).hexdigest()
		
		return {
			'nome': nome,
			'cpf': cpf,
			'telefone': telefone,
			'senha': senha_hash,
			'tipo': tipo,
		}

class UsuarioEditarForm(forms.Form):
	nome 		=	forms.CharField(label='Nome', max_length=100)
	cpf 		=	forms.CharField(label='Nome', max_length=14)
	telefone 	=	forms.CharField(label='Nome', max_length=15)
	senha 		=	forms.CharField(label='Nome', max_length=100, widget=forms.PasswordInput, required=False)
	tipo 		=	forms.CharField(label='Nome', max_length=1)

	def clean_form(self):
		nome 		=	self.cleaned_data.get('nome')
		cpf			= 	self.cleaned_data.get('cpf')
		telefone	=	self.cleaned_data.get('telefone')
		senha		=	self.cleaned_data.get('senha')
		tipo 		=	self.cleaned_data.get('tipo')

		senha_hash = hashlib.sha256(senha.encode()).hexdigest()
		
		return {
			'nome': nome,
			'cpf': cpf,
			'telefone': telefone,
			'senha': senha_hash,
			'tipo': tipo,
		}