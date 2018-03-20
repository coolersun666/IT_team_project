import os
import urllib

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template.context_processors import csrf

from manicurer import models
from manicurer.forms import UserForm, UserProfileForm, UploadForm, CommmentForm
from django.contrib.auth.decorators import login_required
from datetime import datetime, time
from manicurer.models import UserProfile, Picture, Comment
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_protect
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
    response = render(request, 'manicurer/greatest.html', context_dict)
    return response


@login_required
def add_comment(request, name):
    context_dict={}

    try:
        picture = Picture.objects.get(name=name)
        user = request.user
        context_dict['name'] = name
        context_dict['picture'] = picture
    except Picture.DoesNotExist:
        picture = None
    form = CommmentForm(request.POST)
    if form.is_valid():
        comment = form.cleaned_data['comment']
        c = Comment(content=comment, picture = picture)
        c.user = user
        c.save()

        return render(request, 'manicurer/addSuccess.html', context_dict)


@login_required
def like_picture(request):
    picture_name = None
    if request.method == 'GET':
        picture_name = request.GET['picture_name']
    likes = 0
    if picture_name:
        pic = Picture.objects.get(name=str(picture_name))
        if pic:
            likes = pic.NumberOfRates + 1
            pic.NumberOfRates = likes
            pic.save()
            return HttpResponse(likes)



def viewPicture(request,pn):
    context_dict = {}
    comment_form = CommmentForm(request.POST)
    try:
        picture=Picture.objects.get(name=pn)
        comments = Comment.objects.filter(picture=picture)
        picture_list=Picture.objects.filter(name=pn)
        context_dict = {'pictures': picture_list,
                        'name': pn,
                        'comments':comments,
                        'picture':picture,
                        'comment_form':comment_form
                        }
    except Picture.DoesNotExist:
        context_dict['picture'] = None
        context_dict['comments'] = None
    return render(request, 'manicurer/viewPicture.html', context_dict)
    return response


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
    # Handle file upload
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            newPic = Picture(picture = request.FILES['picturefile'],owner=request.user.username,name=request.POST['name'])
            newPic.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect('/manicurer/media/myupload/')
    else:
        form = UploadForm() # A empty, unbound form
    picture_list=Picture.objects.filter(owner=request.user.username)
    # Render list page with the documents and the form
    return render(request,
        'manicurer/myupload.html',
        { 'form': form,'pictures': picture_list},
    )


@login_required
def delete(request,name):
    context_dict = {'user': request.user}


    picture = Picture.objects.get(name=name).delete()

    return HttpResponseRedirect('/manicurer/media/myupload/')






@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))