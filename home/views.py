from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import LoginForm
from .models import *


# Create your views here.
def index(request):
    return render(request, 'home/index.html')


def logout1(request):
    logout(request)
    return HttpResponseRedirect(reverse('home:index'))
