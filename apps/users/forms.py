from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField, AuthenticationForm
from .models import Users
from django.contrib.auth.forms import UserCreationForm


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Users
        fields = ("username",)

    def clean(self):
        cleaned = super().clean()
        if cleaned.get("password1") != cleaned.get("password2"):
            raise forms.ValidationError("Passwords do not match")
        return cleaned

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Users
        fields = ("username", "password", "is_staff", "is_active")


class LoginForm(AuthenticationForm):
    
    username = forms.CharField(
        label='username',
        widget=forms.TextInput(attrs={"class": "form-control","placeholder": "username"})
    )
    password = forms.CharField(
        label='password',
        widget=forms.TextInput(attrs={"class": "form-control","placeholder": "password"})
    )




class RegisterForm(UserCreationForm):

    class Meta:
        model = Users
        fields = ["username", "password1", "password2",]


