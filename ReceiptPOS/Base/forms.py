from django import forms
from .models import *
from .views import *
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Username ', 'class': 'form-control'}))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Password ', 'type': 'password', 'class': 'form-control'}))


class RegistrationForm(forms.Form):
    firstname = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'First name ', 'class': 'form-control'}),
        label='First name')
    lastname = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Last name ', 'class': 'form-control'}),
        label='Last name')
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Username ', 'class': 'form-control'}),
        label='Username')
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Password ', 'class': 'form-control'}),
        label='Password')
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Confirm password ', 'class': 'form-control'}),
        label='Confirm password')
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Email address ', 'class': 'form-control'}),
        label='Email address')


class PasswordChangeForm(forms.Form):
    old_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Old password ', 'type': 'password', 'class': 'form-control'}))
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'New password ', 'type': 'password', 'class': 'form-control'}))
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Confirm password ', 'type': 'password', 'class': 'form-control'}))


class ProfileForm(forms.ModelForm):
    # user = forms.ModelChoiceField(
    #     widget=forms.Select(
    #         attrs={'placeholder': '', 'class': 'form-control'}),
    #     queryset=User.objects.all(),
    #     label='User')

    photo = forms.ImageField(
        widget=forms.ClearableFileInput(
            attrs={'placeholder': '', 'class': 'form-control'}),
        label='Photo')

    about = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Describe yourself', 'class': 'form-control'}),
        label='About')

    birthday = forms.DateField(
        widget=forms.SelectDateWidget(
            attrs={'placeholder': '', 'class': 'form-control'}),
        label='Birthday')

    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Phone number', 'class': 'form-control'}),
        label='Phone')

    class Meta:
        model = UserProfile
        fields = ('photo', 'about', 'birthday', 'phone',)


class ProductForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Nom du produit', 'class': 'form-control'}),
        label='Produit')

    quantity = forms.CharField(
        widget=forms.NumberInput(
            attrs={'placeholder': 'Quantité', 'class': 'form-control'}),
        label='Quantité')

    price = forms.CharField(
        widget=forms.NumberInput(
            attrs={'placeholder': 'Prix', 'class': 'form-control'}),
        label='Prix')

    class Meta:
        model = Products
        fields = ('name', 'quantity', 'price',)


class ClientForm(forms.ModelForm):
    client = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Nom du client', 'class': 'form-control'}),
        label='Client')

    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Phone', 'class': 'form-control'}),
        label='Phone')

    residence = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Residence', 'class': 'form-control'}),
        label='Residence')

    tva = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'TVA/HTVA', 'class': 'form-control'}),
        label='TVA/HTVA')

    nif = forms.CharField(
        widget=forms.NumberInput(
            attrs={'placeholder': 'NIF', 'class': 'form-control'}),
        label='NIF')

    class Meta:
        model = ClientProfile
        fields = ('client', 'phone', 'residence', 'tva', 'nif')


class OrderForm(forms.ModelForm):
    client = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={'placeholder': 'Nom du client', 'class': 'form-control'}),
        queryset=ClientProfile.objects.all(),
        label='Clients')

    class Meta:
        model = OrdersNo
        fields = ('client',)


