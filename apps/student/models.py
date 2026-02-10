from django.db import models


class Parents (models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)


    def __str__(self):
        return self.name
    

# Create your models here.
class Students(models.Model):
    user = models.ForeignKey("users.Users", on_delete=models.CASCADE)
    study_year = models.CharField(max_length=2)
    parents = models.ForeignKey("student.Parents", on_delete=models.CASCADE)
    klass = models.ForeignKey("main.Klass",on_delete=models.CASCADE)
    

    def __str__(self):
        return self.user.username
    
