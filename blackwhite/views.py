from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.

# region 01 Home - Landing Page
def home(request):
    return render(request, 'blackwhite/home.html')
# endregion 01 Home - Landing Page

def loginuser(request):
    pass

def logoutuser(request):
    pass

def signupuser(request):
    pass

