from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from cart import Cart



from .forms import ContactForm, SignUpForm, SimulationForm
# Create your views here.
def home(request): 
	title = 'Welcome'
	form = SignUpForm(request.POST or None)
	context = {
		"title": title,
		"form": form
	}

	
	if form.is_valid():
		# form.save()
		instance = form.save(commit=False)
		
		full_name = form.cleaned_data.get("full_name")
		if not full_name:
			full_name = "New full name"
		instance.full_name = full_name

		# if not instance.full_name:
		# 	instance.full_name = "Justin"
		instance.save()
		context = {
			"title": "Thank you"
		}
		
	return render(request, "home.html", context)

def contact(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		# for key in form.cleaned_data:
		# 	print key
		# 	print form.cleaned_data.get(key)
		form_email = form.cleaned_data.get("email")
		form_mensagem = form.cleaned_data.get("mensagem")
		form_nome = form.cleaned_data.get("nome")
		# print email, message, full_name
		subject = 'Contacto Insurance4all'
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email, 'baiaodjango@gmail.com']
		contact_message = "%s: %s via %s"%(
			form_nome, 
			form_mensagem, 
			form_email)
		some_html_message = """
		<h1>hello</h1>
		"""
		send_mail(subject, 
				  contact_message, 
				  from_email, 
				  to_email, 
				  fail_silently=True)
	
	context = {
		"form": form,
	}

	return render(request, "forms.html", context)

def simulation(request):
	form= SimulationForm(request.POST or None)
	if form.is_valid():
		# for key, value in form.cleaned_data.iteritems():
		# 	print key, value
			# print form.cleaned_data.get(key)
		form_categoria = form.cleaned_data.get("category")
		form_Nome = form.cleaned_data.get("name")
		form_Valor = form.cleaned_data.get("Valor")
		# print email, message, full_name
		instance = form.save(commit=False)
		instance.save()
	context = {
		"form": form,
	}

	return render(request, "simularform.html", context)




