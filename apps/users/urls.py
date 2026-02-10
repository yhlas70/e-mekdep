from django.urls import path
from .views import Login, register

urlpatterns = [
    path('login/', Login.as_view(),name='login'),
    path('register/',register),

]