from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Art
from .forms import ArtForm
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
        form.save()
        return HttpResponseRedirect('/')
    else:
        form = ArtForm()
        return render_to_response ('index.html', {'form': form})

    #return render(request, 'index.html', {'form': form})
        #arts = Art(name=form.cleaned_data['name'],
                   #img_url = form.cleaned_data['img_url'],
                   #medium = form.cleaned_data['medium'],
                   #description = form.cleaned_data['description'])
        #arts.save()
        #return HttpResponse('image upload success')
    #return HttpResponseRedirect('/')
