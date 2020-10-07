# Add the following import
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Bird 
from .forms import Bird_Form


# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello Birds</h1>')

def about(request):
    return render(request, 'about.html')




# index and create
def birds_index(request):
    if request.method == 'POST':
        bird_form = Bird_Form(request.POST)
        if bird_form.is_valid():
            bird_form.save()
            return redirect('birds_index')
    birds = Bird.objects.all()
    bird_form = Bird_Form()
    context = {'birds': birds, 'bird_form': bird_form}
    return render(request, 'birds/index.html', context)





# show 
def birds_detail(request,bird_id):
    bird = Bird.objects.get(id=bird_id)
    return render(request, 'birds/detail.html',{'bird':bird})


# edit && update
def birds_edit(request, bird_id):
  bird = Bird.objects.get(id=bird_id)
  if request.method == 'POST':
    bird_form = Bird_Form(request.POST, instance=bird)
    if bird_form.is_valid():
      bird_form.save()
      return redirect('detail', bird_id=bird_id)
  else:  
    # in form(instance=The object that we pull back from db)
    bird_form = Bird_Form(instance=bird)
    context = {'bird': bird, 'bird_form': bird_form}
    return render(request, 'birds/edit.html', context)






# delete
def birds_delete(request, bird_id):
    Bird.objects.get(id=bird_id).delete()
    return redirect("birds_index")