from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
from .models import *
from django.urls import reverse


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(null=True, blank=True, upload_to="photo/")
    birthday = models.DateField(null=True, blank=True, max_length=100)
    about = models.CharField(null=True, blank=True, max_length=50)
    phone = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ['user']

    def __str__(self):
        return f"{self.user.username}"


class ClientProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    client = models.CharField(null=True, blank=True, max_length=100)
    phone = models.CharField(null=True, blank=True, max_length=100)
    residence = models.CharField(null=True, blank=True, max_length=50)
    # tva = models.CharField(null=True, blank=True, max_length=50)
    nif = models.CharField(null=True, blank=True, max_length=50)

    class Meta:
        ordering = ['client']

    def __str__(self):
        return f"{self.client} - {self.phone}"


class Products(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(null=True, blank=True, max_length=50)
    quantity = models.IntegerField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name}"


class OrdersNo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    no = models.CharField(null=True, blank=True, max_length=50)
    quantity = models.CharField(null=True, blank=True, max_length=50)
    price = models.CharField(null=True, blank=True, max_length=50)
    client = models.ForeignKey(ClientProfile, verbose_name="Client name", on_delete=models.CASCADE)
    name = models.ForeignKey(Products, verbose_name="Product name", on_delete=models.CASCADE)

    class Meta:
        ordering = ['no']

    def __str__(self):
        return f"{self.no} - {self.client}"



