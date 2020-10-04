# Add the following import
from django.shortcuts import render
from django.http import HttpResponse 


# Create your views here.
# Define the home view
def home(request):
    return HttpResponse('<h1>Hello Birds</h1>')

def about(request):
    return render(request, 'about.html')



class Bird:
    def __init__(self, name,description,color, age):
        self.name = name
        self.description = description
        self.color = color
        self.age = age


birds = [
Bird('Parrots', 'also known as psittacines and found mostly in tropical and subtropical regions', 'red and blue', 2),
Bird('Owls', 'tube-shaped eyes are completely immobile, providing binocular vision which fully focuses on their prey and boosts depth perception', 'dark-dotted and grey', 1),
Bird('Songbirds', 'another name that is sometimes seen as the scientific or cernacular name is Oscines Latin Oscen A song bird', 'yellow and dark', 3)
]






def birds_index(request):
    context = {'birds':birds}
    return render(request, 'birds/index.html' , context)
