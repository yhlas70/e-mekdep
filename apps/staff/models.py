from django.db import models
from apps.users.models import Users
from .enums import Role

class Staff(models.Model):
    
    user = models.ForeignKey("users.Users", on_delete=models.CASCADE)
    degree = models.CharField(max_length=50)
    role = models.CharField(choices=Role.choices, max_length=50,null=True,blank=True)

    def __str__(self):
        return self.degree + self.user.name
    