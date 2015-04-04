from django.shortcuts import render, get_object_or_404
from .models import Cat
# Create your views here.

def about(request):
    cat = Cat.objects.filter(pict_url__startswith='http:/').order_by('?')[0]
    return render(request, 'cats/about.html', {'cat':cat})

def adoptable_list(request):
    cats= Cat.objects.filter(adopted=False).order_by('name')
    return render(request, 'cats/adoptable.html',{'cats':cats})

def detail(request, id):
    cat = get_object_or_404(Cat, id=id)
    return render(request, 'cats/detail.html', {'cat':cat})
