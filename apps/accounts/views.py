from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model, authenticate, login, logout
from apps.accounts.forms import LoginForm, RegistrationForm
# from django.views.decorators.csrf import csrf_exempt 


User = get_user_model()
# Create your views here.

# class RegistrationView(TemplateView, LoginRequiredMixin):


class RegistrationView(TemplateView):
    template_name = 'accounts/registration.html'

    def get(self, request, *args, **kwargs):
        # 1. Proactively redirect logged-in users away
        if request.user.is_authenticated:
            return redirect('news:home')
            
        # 2. Instantiate an empty form for the initial GET request
        context = self.get_context_data(**kwargs)
        context['form'] = RegistrationForm()
        return self.render_to_response(context)
    
    
    def post(self, request, *args, **kwargs):
        # 1. Bind incoming POST data to your form class
        form = RegistrationForm(request.POST)
        
        # 2. Run Django's field validations
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()  # Save the user instance to the database
            messages.success(
                request,
                "Muvaffaqiyatli ro'yxatdan o'tdingiz!"
            )
            return redirect('accounts:login')
        
        # 3. If form is invalid, re-render with errors
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return self.render_to_response(context)

class LoginView(TemplateView):
    template_name = 'accounts/login.html'
    def get(self, request, *args, **kwargs):
        # 1. Proactively redirect logged-in users away
        if request.user.is_authenticated:
            return redirect('news:home')
            
        # 2. Instantiate an empty form for the initial GET request
        context = self.get_context_data(**kwargs)
        context['form'] = LoginForm()
        return self.render_to_response(context)
    # @csrf_exempt
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
                messages.success(
                request,
                "Muvaffaqiyatli login qilindi!"
            )
                return redirect('news:home')
            else:
                messages.error(
                    request,
                    "Username yoki parol noto‘g‘ri!"
                )
                form.add_error(None, "Invalid username or password.")
                
        # 4. If form is invalid or authentication failed, re-render with errors
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return self.render_to_response(context)
    

class LogoutView(TemplateView, LoginRequiredMixin):
    # template_name = 'accounts/logout.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)
            messages.success(
            request,
            "Muvaffaqiyatli logout qilindi!"
            )
        return redirect('news:home')
