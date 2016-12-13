from django.shortcuts import render
from .models import Art

def index(request):
    arts = Art.objects.all()
    return render(request, 'index.html',{'arts': arts})
# Create your views here.
