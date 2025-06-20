from django.db import models
from django.utils import timezone


from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
    )


class StudentManager(BaseUserManager):
    def create_user(self,name,email,password=None,**extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        if not name:
            raise ValueError("Users must have an email address")
        
        email=self.normalize_email(email)
        user= self.model(name=name,email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,name,email,password,**extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        return self.create_user(name, email, password, **extra_fields)

class Student(AbstractBaseUser,PermissionsMixin):
    name = models.CharField(max_length=100,blank=False,null=False)
    email = models.EmailField(max_length=50,unique=True,blank=False,null=False)
    
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]
    
    objects = StudentManager()
    
    def __str__(self):
        return self.name