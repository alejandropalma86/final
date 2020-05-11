from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .forms import ContactForm


class ContactView(View):
    template_name = 'contact/contact.html'
    def get(self, request):
        return render(request, self.template_name, dict(form=ContactForm))

    def post(self, request):
        data = request.POST
        form = ContactForm(data)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            content = form.cleaned_data.get('content')
            #Envíamos el correo y direccionamos
            email = EmailMessage(
                subject ='APPSolutions: Nuevo mensaje de contacto',
                body = 'De: {} <{}>\n\nEscribió:\n\n{}'.format(name, email, content),
                from_email='no-contestar@inboxmailtrap.io',
                to=['alisterpalma@hotmail.com'],
                reply_to=[email],
            )
            try:
                email.send()
                #Todo ha ido bien
                return redirect(reverse('contact')+'?ok')
            except:
                #Algo no ha ido bien redireccionar a Fail
                return redirect(reverse('contact')+'?fail')
        return render(request,self.template_name, dict(form=form))
