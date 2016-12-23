from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import Art
from .forms import ArtForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.forms.models import model_to_dict
from django.core.urlresolvers import reverse


def index(request):
    arts = Art.objects.all()
    form = ArtForm()
    return render(request, 'index.html',{'arts': arts, 'form': form})

def detail(request, art_id):
    arts = Art.objects.get(id=art_id)
    return render(request, 'detail.html', {'arts': arts})

def post_art(request):
    if request.method == 'POST':
        form = ArtForm(request.POST, request.FILES)
    if form.is_valid():
        art = form.save(commit = False)
        art.user=request.user
        art.save()
        return HttpResponseRedirect('/')
    else:
        form = ArtForm()
        return render_to_response ('index.html', {'form': form})

def edit(request, art_id):
    arts = Art.objects.get(id=art_id)
    if (request.method == 'POST'):
        # Process the form
        form = ArtForm(request.POST, request.FILES, instance=arts)
        if form.is_valid():
            form.save(commit = True)
            return redirect(reverse('detail', args=[art_id,]))

    else:
        art_dict = model_to_dict(arts)
        form = ArtForm(art_dict)
        return render(request, 'edit.html', {'form':form})


def profile(request, username):
    user = User.objects.get(username=username)
    arts = Art.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'arts': arts})

def login_view(request):
    if request.method=="POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['Password']
            user = authenticate (username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return HttpResponseRedirect('/')
                else:
                    return HttpResponse("The account has been disabled!")
            else:
                return HttpResponse("The username and password were incorrect!")
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form} )


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
