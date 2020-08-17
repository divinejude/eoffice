from django.shortcuts import render, redirect
from django.views.generic import View
from home.forms import LoginForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.views.generic.edit import CreateView
from home.models import File
from django.views import generic

# Create your views here.
class FileIndexView(generic.ListView):
    template_name = 'ssg/s_dashboard.html'
    context_object_name = 'all_files'

    def get_queryset(self):
        return File.objects.all()
