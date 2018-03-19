import os

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from manicurer.forms import UserForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from datetime import datetime, time
from manicurer.models import UserProfile, Picture


# Create your views here.
def index(request):
    picture_list = Picture.objects.order_by('-NumberOfRates')[:3]
    context_dict = {'pictures': picture_list}
    response = render(request, 'manicurer/index.html', context_dict)
    return response

def about(request):

    context_dict = {}
    return render(request, 'manicurer/about.html', context_dict)

def contact(request):

    context_dict = {}
    return render(request, 'manicurer/contact.html', context_dict)

def greatest(request):
    picture_list = Picture.objects.order_by('-avgrate')[:4]
    context_dict = {'pictures': picture_list}
    response = render(request, 'manicurer/index.html', context_dict)
    return response


@login_required
def like_Picture(request):
    pic_name=None
    if request.method == 'GET':
        pic_name = request.GET.get['Picture_name']

    likes=0

    if pic_name:
        pic = Picture.objects.get(name=str(pic_name))
        if pic:
            likes = pic.NumberOfRates + 1
            pic.NumberOfRates = likes
            pic.save()
    return HttpResponse(likes)


def hotest(request):
    picture_list = Picture.objects.order_by('-NumberOfRates')[:4]
    context_dict = {'pictures': picture_list}
    return render(request, 'manicurer/hotest.html', context_dict)

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
                profile.save()
                registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request, 'manicurer/register.html',
                  {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your Manicurer account is disabled.")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'manicurer/login.html', {})

def some_view(request):
    if not request.user.is_authenticated():
        return HttpResponse("You are logged in.")
    else:
        return HttpResponse("You are not logged in.")

@login_required
def myupload(request):
    myuploaded = False
    if request.method == 'POST':
        upload_form = UserProfileForm(data=request.POST)
        if upload_form.is_valid() :
            uploading = upload_form.save()

            file = upload_form.save(commit=False)

            if 'picture' in request.FILES:
                file.picture = request.FILES['picture']
                file.save()
                myuploaded = True
        else:
            print(upload_form.errors)
    else:

        upload_form = UserProfileForm()
    return render(request, 'manicurer/register.html',
                  {'profile_form': upload_form, 'myuploaded': myuploaded})




@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))