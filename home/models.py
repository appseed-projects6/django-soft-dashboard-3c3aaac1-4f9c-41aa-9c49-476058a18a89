# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    bio = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Customer_Info(models.Model):

    #__Customer_Info_FIELDS__
    first_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)

    #__Customer_Info_FIELDS__END

    class Meta:
        verbose_name        = _("Customer_Info")
        verbose_name_plural = _("Customer_Info")


class Order(models.Model):

    #__Order_FIELDS__

    #__Order_FIELDS__END

    class Meta:
        verbose_name        = _("Order")
        verbose_name_plural = _("Order")


class Product(models.Model):

    #__Product_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)

    #__Product_FIELDS__END

    class Meta:
        verbose_name        = _("Product")
        verbose_name_plural = _("Product")



#__MODELS__END
