from django import forms

from .models import SignUp, simulation

class ContactForm(forms.Form):
	Nome_Inteiro = forms.CharField(required=False)
	email = forms.EmailField()
	Mensagem = forms.CharField()

class ContactForm(forms.Form):
	Nome = forms.CharField()
	email = forms.EmailField()
	Mensagem = forms.CharField()

class SimulationForm(forms.ModelForm):
	class Meta:
		model = simulation
		fields = ["Categoria", "Nome", "Valor"]
	
	def clean_Nome(self):
		Nome = self.cleaned_data.get("Nome")
		return Nome 

	

class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = ["full_name", "email"]

	def clean_email(self):
		email = self.cleaned_data.get("email")
		email_base, provider = email.split("@")
		domain, extension = provider.split('.')
		# if not domain == 'USC':
		# 	raise forms.ValidationError("Please make sure you use your USC email.") 
		if not extension == "edu":
			raise forms.ValidationError("Please use a valid .edu email adress")
		return email

	def clean_full_name(self):
		full_name = self.cleaned_data.get('full_name')
		#write validation code
		return full_name
