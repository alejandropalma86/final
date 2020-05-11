from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views import View
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.utils import timezone
from .forms import RegisterForm, LoginForm



class RegisterView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('vacancy')
        template_name ='register.html'
        return render(request, template_name, dict(form=RegisterForm))

    def post(self, request):
        template_name = 'register.html'
        data = request.POST
        form = RegisterForm(data)
        if form.is_valid():
            cd = form.cleaned_data
            user = form.save()
            login(request, user)
            messages.success(request, 'Registro con éxito')
            return redirect('vacancy')
        else:
            messages.error(request, 'Ingreso de datos incorrectos')
            for field in form.errors:
                form.fields[field].widget.attrs['class'] = 'input is-danger'

            return render(request, template_name, dict(form=form))


class LoginView(View):
    template_name = 'login.html'
    def get(self, request):
        return render(request, self.template_name, dict(form=LoginForm))

    def post(self, request):
        data = request.POST
        form = LoginForm(data)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('vacancy')
            
        messages.error(request, 'Usuario o contraseña incorrectos')
        return render(request, self.template_name, dict(form=form))

            
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')




