from django import forms
import hashlib

class LoginForm(forms.Form):
	cpf = forms.CharField(label='CPF', max_length=14)
	senha = forms.CharField(label='Senha', max_length=100, widget=forms.PasswordInput)

	def clean_form(self):
		cpf = self.cleaned_data.get('cpf')
		senha = self.cleaned_data.get('senha')

		senha_hash = hashlib.sha256(senha.encode()).hexdigest()

		return {
			'cpf': cpf,
			'senha': senha_hash,
		}

class TrocarSenhaForm(forms.Form):
	cpf 			= forms.CharField(label='CPF', max_length=14)
	nova_senha 		= forms.CharField(label='Nova senha', max_length=100, widget=forms.PasswordInput)
	confirma_senha 	= forms.CharField(label='Confirmar senha', max_length=100, widget=forms.PasswordInput)

	def clean_form(self):
		cpf 				= self.cleaned_data.get('cpf')
		nova_senha 			= self.cleaned_data.get('nova_senha')
		confirma_senha 		= self.cleaned_data.get('confirma_senha')

		nova_senha_hash 	= hashlib.sha256(nova_senha.encode()).hexdigest()
		confirma_senha_hash = hashlib.sha256(confirma_senha.encode()).hexdigest()

		return {
			'cpf': cpf,
			'nova_senha': nova_senha_hash,
			'confirma_senha': confirma_senha_hash,
		}

class RedefinirForm(forms.Form):
	cpf = forms.CharField(label='CPF', max_length=14)

	def clean_form(self):
		cpf = self.cleaned_data.get('cpf')
		
		return { 'cpf': cpf }