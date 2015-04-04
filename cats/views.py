from django.shortcuts import render
from .models import Cat
# Create your views here.

def about(request):
    return render(request, 'cats/about.html', {})

def adoptable_list(request):
    cats= Cat.objects.filter(adopted=False).order_by('name')
    return render(request, 'cats/adoptable.html',{'cats':cats})
