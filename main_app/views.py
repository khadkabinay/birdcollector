# Add the following import
from django.shortcuts import render
from django.http import HttpResponse
from .models import Bird 


# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello Birds</h1>')

def about(request):
    return render(request, 'about.html')




def birds_index(request):
    birds = Bird.objects.all()
    context = {'birds':birds}
    return render(request, 'birds/index.html' , context)


def birds_detail(request,bird_id):
    bird = Bird.objects.get(id=bird_id)
    return render(request, 'birds/detail.html',{'bird':bird})