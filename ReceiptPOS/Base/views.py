from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import *
from .models import *
from .views import *
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.files import File
from django.contrib.auth.forms import PasswordChangeForm
from django.utils.datastructures import MultiValueDictKeyError
from django.db.models import Count

# Create your views here.


def connect(request):
    header_title = "Login"
    form = LoginForm(request.POST)
    try:
        next_p = request.GET["next"]
    except:
        next_p = ""
    if request.method == "POST" and form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.error(request, "You're now connected!")
            if next_p:
                return redirect(next_p)
            else:
                return redirect(index)
        else:
            messages.warning(request, "Connection failed !")
    form = LoginForm()
    return render(request, 'login.html', locals())


def registration(request):
    header_title = "Register"
    if request.method == "POST":
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data['username']
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            password = form.cleaned_data['password']
            password2 = form.cleaned_data['password2']
            email = form.cleaned_data['email']
            if password == password2:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password)
                user.first_name, user.last_name = firstname, lastname
                user.save()
                messages.success(request, "Hello " + username + ", youn are registered successfully!")
                if user:
                    login(request, user)
                    return redirect(index)
    form = RegistrationForm()
    return render(request, 'registration.html', locals())


@login_required
def index(request):
    header_title = "Welcome"
    prof = UserProfile.objects.filter(user=request.user)

    return render(request, "index.html", locals())


@login_required
def profileview(request):
    header_title = "Update your profile"
    if request.method == "POST":
        form = ProfileForm(request.POST or None, request.FILES)
        if form.is_valid():
            u = request.user
            ph = form.cleaned_data['photo']
            b = form.cleaned_data['birthday']
            a = form.cleaned_data['about']
            p = form.cleaned_data['phone']
            UserProfile(user=u, photo=ph, birthday=b, about=a, phone=p).save()
            messages.success(request, "Profile updated successfully!")

    form = ProfileForm()
    return render(request, "profiles.html", locals())


@login_required
def addProduct(request):
    header_title = "Ajouter un produit"
    if request.method == "POST":
        form = ProductForm(request.POST or None, request.FILES)
        if form.is_valid():
            u = request.user
            n = form.cleaned_data['name']
            q = form.cleaned_data['quantity']
            p = form.cleaned_data['price']
            Products(user=u, name=n, quantity=q, price=p).save()
            messages.success(request, "Produit ajouté avec succès!")

    form = ProductForm()
    return render(request, "addproducts.html", locals())


@login_required
def productList(request):
    usr = ClientProfile.objects.all()
    header_title = "Liste des produits"
    order = OrdersNo.objects.all().count()
    neworder = order + 1
    getDataList = Products.objects.all()
    i = request.POST.getlist('checks[]')    #We check selected checkbox
    ii = request.POST.getlist('checks1[]')  #We look for quantity
    form = OrderForm(request.POST)
    if form.is_valid():
        for x in i:
            for xx in ii:
                if not xx == "":
                    pro = Products.objects.get(id=x)
                    u = request.user
                    cl = form.cleaned_data['client']
                    # if xx > pro.quantity:
                    #     print("Quantity is big !")
                    # else:

                    print(u, cl, pro, neworder, xx)
                    # OrdersNo(user=u, client=cl, name=pro, no=neworder, quantity=xx).save()
                    # messages.success(request, "Enregistré avec succès !")
        messages.success(request, "Enregistré avec succès !")

    return render(request, "productlist.html", locals())


@login_required
def orderList(request):
    header_title = "Liste des ventes"
    myOrder = OrdersNo.objects.all().order_by('no')
    return render(request, "orderlist.html", locals())


@login_required
def orderDetail(request, id, idd):
    header_title = "Factures"
    detOrder = get_object_or_404(OrdersNo, id=id)
    productData = get_object_or_404(Products, id=idd)
    pr = productData.price

    loo = OrdersNo.objects.filter(no=detOrder.no)

    return render(request, "orderDetail.html", locals())


@login_required
def addClient(request):
    header_title = "Ajouter un client"
    if request.method == "POST":
        form = ClientForm(request.POST or None, request.FILES)
        if form.is_valid():
            u = request.user
            c = form.cleaned_data['client']
            r = form.cleaned_data['residence']
            p = form.cleaned_data['phone']
            t = form.cleaned_data['tva']
            n = form.cleaned_data['nif']

            ClientProfile(user=u, client=c, residence=r, phone=p, tva=t, nif=n).save()
            messages.success(request, "Client ajouté avec succès!")

    form = ClientForm()
    return render(request, "addclients.html", locals())


def disconnect(request):
    logout(request)
    return redirect(index)


@login_required
def changePassword(request):
    prof = UserProfile.objects.filter(user=request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })


@login_required
def saleview(request):
    usr = ClientProfile.objects.all()
    header_title = "Liste des produits"
    order = OrdersNo.objects.all().count()
    neworder = order + 1
    getDataList = Products.objects.all()
    i = request.POST.getlist('checks[]')    #We check selected checkbox
    ii = request.POST.getlist('checks1[]')  #We look for quantity
    form = OrderForm(request.POST)
    # if form.is_valid():
    #     for x in i:
    #         for xx in ii:
    #             if not xx == "":
    #                 pro = Products.objects.get(id=x)
    #                 u = request.user
    #                 cl = form.cleaned_data['client']
                    # if xx > pro.quantity:
                    #     print("Quantity is big !")
                    # else:

                    # print(u, cl, pro, neworder, xx)
                    # OrdersNo(user=u, client=cl, name=pro, no=neworder, quantity=xx).save()
                    # messages.success(request, "Enregistré avec succès !")
        # messages.success(request, "Enregistré avec succès !")

    return render(request, "sale.html", locals())


# def check(a, p, p1):
#     if a.endswith("@gmx.com") or a.endswith("@hotmail.com") or a.endswith("@gmail.com") or a.endswith(
#             "@yahoo.fr") or a.endswith("@outlook.com") or a.endswith("@icloud.com") or a.endswith("@protonmail.com"):
#         if p == p1:
#             auths.create_user_with_email_and_password(a, p)
#             print("Welcome to YoMoney")
#
#         else:
#             print("Passwords don't match !")
#     else:
#         print("Your email is not supported !")
