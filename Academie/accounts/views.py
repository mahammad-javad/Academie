from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages
from django.utils.crypto import get_random_string
from .forms import RegisterForm, LoginForm
from .models import User
from utils.email_utils import send_custom_email
from django.urls import reverse


def user_panel_sidebar(request):
    return render(request, 'includes/sidebar.html')


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'accounts/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User(
                full_name=form.cleaned_data['full_name'],
                email=form.cleaned_data['email'],
                username=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                is_active=False,
                activation_code=get_random_string(72)
            )
            user.set_password(form.cleaned_data['password'])
            user.save()

            activation_link = request.build_absolute_uri(
                reverse('activate_account', args=[user.activation_code])
            )

            send_custom_email(
                subject='فعالسازی حساب کاربری',
                to=user.email,
                context={
                    'user': user,
                    'activation_link': activation_link
                },
                template_name='emails/activate_account.html'
            )

            return redirect('home')

        return render(request, 'accounts/register.html', {'form': form})



class LoginView(View):
    template_name = 'accounts/login.html'

    def get(self, request):
        form = LoginForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            login(request, user)
            return redirect('home')  # بعد از ورود کاربر به صفحه اصلی هدایت شود
        return render(request, self.template_name, {'form': form})



class ActivateAccountView(View):
    def get(self, request, code):
        user = User.objects.filter(activation_code=code).first()
        if user:
            user.is_active = True
            user.activation_code = None
            user.save()
            return redirect('login_page')
        messages.error(request,'خطایی رخ داد')
        return render(request, 'accounts/login.html')



class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login_page')


class UserPanelView(View):
    def get(self, request):
        return render(request, 'accounts/dashboard.html')


