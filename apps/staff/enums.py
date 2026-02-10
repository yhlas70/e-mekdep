from django.db import models

class Role(models.TextChoices):
    Student = 'STUDENT', 'student'
    Teacher = 'Teacher', 'teacher'

    