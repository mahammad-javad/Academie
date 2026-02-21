from django import forms
from django.contrib.auth import authenticate
from django.core import validators
from .models import User


class RegisterForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'رمز عبور'}),
        validators=[validators.MaxLengthValidator(100)],
        label='رمز عبور'
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'تکرار رمز عبور'}),
        validators=[validators.MaxLengthValidator(100)],
        label='تکرار رمز عبور'
    )

    class Meta:
        model = User
        fields = ['full_name', 'email', 'phone']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام کامل'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'شماره موبایل'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError('این ایمیل قبلاً ثبت شده است')
        return email

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm = self.cleaned_data.get('confirm_password')
        if password != confirm:
            raise forms.ValidationError('رمز عبور و تکرار آن یکسان نیست')
        return confirm


class LoginForm(forms.Form):
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'ایمیل خود را وارد کنید'})
    )
    password = forms.CharField(
        label='کلمه عبور',
        widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'کلمه عبور خود را وارد کنید'})
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            user = authenticate(username=email, password=password)
            if not user:
                raise forms.ValidationError("ایمیل یا کلمه عبور اشتباه است")
            if not user.is_active:
                raise forms.ValidationError("حساب کاربری شما فعال نیست")
            cleaned_data['user'] = user
        return cleaned_data