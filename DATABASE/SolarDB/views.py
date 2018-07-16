from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.sessions.models import Session

from .models import User
from .models import Post
import fpdf
import os
import datetime
from fpdf import FPDF

# Create your views here.
def index(request):
    

    context = {}
    if request.method == "POST":
        if 'login' in request.POST:
            try:
                user = User.objects.get(username=request.POST['username'], password=request.POST['password'])
                
                print(user)

                request.session['user'] = user.pk
                #request.session['accountType'] = user.get_type()
                return HttpResponseRedirect('homepage')

            except User.DoesNotExist:
                context['log_error'] = 'Cannot find an account with that combination.'
                
    if 'register' in request.POST:
            try:
                user = User.objects.get(username=request.POST['username'])
                context['reg_error'] = 'That username is already taken.'
            except User.DoesNotExist:
                user = User(username=request.POST['username'], password=request.POST['password']
                           )
                user.save()
                context['reg_success'] = "Account has been created."
            return render(request, 'register.html', context)
                
    return render(request, 'login.html', context)

def homepage(request):
    context = {}
    return render(request, 'homepage.html', context)
def displaypost(request):
    context = {}
    return render(request, 'maps.html', context)

def addpost(request):
    context = {}
    return render(request, 'maps_form.html', context)


def logout(request):
    print(request.POST)
    if 'logout' in request.POST:
        if 'user' in request.session:
            del request.session['user']
            return HttpResponseRedirect('/')
    
    return HttpResponseRedirect('/')
