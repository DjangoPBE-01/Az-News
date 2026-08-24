from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model, authenticate, login
from apps.accounts.forms import LoginForm


User = get_user_model()
# Create your views here.

# class RegistrationView(TemplateView, LoginRequiredMixin):

class LoginView(TemplateView):
    template_name = 'accounts/login.html'
    def get(self, request, *args, **kwargs):
        # 1. Proactively redirect logged-in users away
        if request.user.is_authenticated:
            return redirect('dashboard')
            
        # 2. Instantiate an empty form for the initial GET request
        context = self.get_context_data(**kwargs)
        context['form'] = LoginForm()
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        # 1. Bind incoming POST data to your form class
        form = LoginForm(request.POST)
        
        # 2. Run Django's field validations
        if form.is_valid():
            email= form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            
            # 3. Authenticate with the database backend
            user = authenticate(request, email=email, password=password)
            
            if user is not None:
                login(request, user)  # Creates the session and cookie
                return redirect('dashboard')
            else:
                form.add_error(None, "Invalid username or password.")
                
        # 4. If form is invalid or authentication failed, re-render with errors
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return self.render_to_response(context)
