from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.db import IntegrityError
from services.authentication.forms import customUserCreationform

class Authentication:
    @staticmethod
    def get_signup(request):
        if request.method == 'GET':
            # Crear una nueva instancia del formulario en GET
            return render(request, 'signup.html', {
                'form': customUserCreationform()  # Instancia del formulario
            })
        elif request.method == 'POST':
            # Crear una instancia del formulario con los datos enviados
            form = customUserCreationform(request.POST)
            if form.is_valid():
                try:
                    user = form.save()
                    login(request, user)
                    return redirect('logged')
                except IntegrityError:
                    # Si ocurre un error de integridad (por ejemplo, nombre de usuario duplicado)
                    return render(request, 'signup.html', {
                        'form': form,
                        'error': 'Unable to register. Please try again later.'
                    })
            else:
                # Si el formulario no es válido, muestra los errores
                return render(request, 'signup.html', {
                    'form': form,
                    'error': 'Please correct the errors below.'
                })
        
    @staticmethod
    def get_signout(request):
        logout(request)
        return redirect('home')
    
    @staticmethod
    def get_signing(request):
        if request.method == 'GET':
            return render(request, 'login.html', {
                'form': AuthenticationForm()
            })
        elif request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                return redirect('logged')
            else:
                return render(request, 'login.html', {
                    'form': form,
                    'error': 'Invalid username or password. Please try again.'
                })

    @staticmethod
    def get_logged(request):
        return render(request, 'logged.html')
    
    def dispatch(self, request, *args, **kwargs):
        match request.path:
            case "/signup":
                return self.get_signup(request)
            case "/login":
                return self.get_signing(request)
            case "/logout":
                return self.get_signout(request)
            case "/logged":
                return self.get_logged(request)
            case "/":
                return self.get(request)
            case _:
                return self.get(request)