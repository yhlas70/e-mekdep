from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from .managers import UserManager

class Users(AbstractBaseUser, PermissionsMixin):
    
    username = models.CharField(max_length=255,unique=True,null=False,blank=False)
    name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField( max_length=255,null=True,blank=True)
    father_name = models.CharField(max_length=255,null=True,blank=True)
    avatar = models.FileField(upload_to="avatarts",null=True, blank=True)
    birthday = models.DateField(null=True,blank=True)
    is_student = models.BooleanField(default=True,null=False,blank=True)



    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []


    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def str(self):
        return self.username