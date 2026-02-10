from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import (
    Grades,

)

@login_required(login_url='/user/login')
def index(request):
    grades = Grades.objects.all()

    user = request.user
    user = user.is_student
    

    return render (request,'index.html',{"grades":grades})

