from django.db import models
from apps.users.models import Users
from .enums import Indexes

class Subjects(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name 
    
class Register(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class Klass(models.Model):
    study_year = models.CharField(max_length=2)
    index = models.CharField(choices=Indexes.choices,max_length=1)
    register = models.ForeignKey("main.Register", related_name="klass", on_delete=models.CASCADE,null=True,blank=True)
    
    @property
    def name(self):
        return self.study_year + self.index
    
    def __str__(self):
        return self.study_year + " " + self.index
    
class Grades (models.Model):
    subject = models.ForeignKey(to=Subjects, on_delete=models.CASCADE)
    student = models.ForeignKey("student.Students", on_delete=models.CASCADE)
    grade =  models.IntegerField()

    def __str__(self):
        a = self.grade
        a = str(a)
        return a +" " +  self.student.user.username