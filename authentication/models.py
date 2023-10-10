from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser
from django.core.validators import RegexValidator
from rest_framework_simplejwt.tokens import RefreshToken
from helper.models import CreationModificationBase
import messages

class UserManager(BaseUserManager):
    def create_user(self, mobile, password=None,**extra_fields):
        if not mobile:
            raise ValueError('Users must have a mobile number')
        user = self.model(mobile=mobile, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, mobile, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(mobile, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin,CreationModificationBase):
    mobile_regex = RegexValidator( regex = r'^[6-9]\d{9}$', message = messages.UPTO_10_DIGIT)
    mobile = models.CharField(max_length = 10, unique = True, validators = [mobile_regex], error_messages={"unique": "Mobile number is already registered"})
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'mobile'
    
    def get_tokens(self):
        """Returns a tuple of JWT tokens (token, refresh_token)"""
        refresh = RefreshToken.for_user(self)
        return str(refresh.access_token), str(refresh)