from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Art
from .forms import ArtForm
from django.contrib.auth.models import User
#from django.template import RequestContext
#from django.core.urlresolvers import reverse



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

def profile(request, username):
    user = User.objects.get(username=username)
    arts = Art.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'arts': arts})
