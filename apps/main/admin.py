from django.contrib import admin
from .models import (
    Subjects,
    Register,
    Klass,
    Grades,
)


admin.site.register(Subjects)
admin.site.register(Register)
admin.site.register(Klass)
admin.site.register(Grades)