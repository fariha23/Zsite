from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Art
from .forms import ArtForm

def index(request):
    arts = Art.objects.all()
    form = ArtForm()
    return render(request, 'index.html',{'arts': arts, 'form': form})

def detail(request, art_id):
    arts = Art.objects.get(id=art_id)
    return render(request, 'detail.html', {'arts': arts})


def post_art(request):
    form = ArtForm(request.POST)
    if form.is_valid():
        arts = Art(name=form.cleaned_data['name'],
                   img_url = form.cleaned_data['img_url'],
                   medium = form.cleaned_data['medium'],
                   description = form.cleaned_data['description'])
        arts.save()
    return HttpResponseRedirect('/')
