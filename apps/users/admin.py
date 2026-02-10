from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Users
from .forms import UserCreationForm, UserChangeForm

@admin.register(Users)
class UserAdmin(BaseUserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = Users

    list_display = ("username", "is_staff", "is_active")
    ordering = ("username",)
    search_fields = ("username",)

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Status", {"fields": ("is_active",)}),
        ("birthday",{"fields":("birthday",)}),
        ("name",{"fields":("name",)}),
        ("last_name",{"fields":("last_name",)}),
        ("father_name",{"fields":("father_name",)}),
        ("avatar",{"fields":("avatar",)})
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "password1", "password2", "is_staff", "is_superuser","birthday"),
        }),
    )