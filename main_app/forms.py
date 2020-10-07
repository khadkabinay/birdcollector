from django.forms import ModelForm
from .models import Bird , Feeding


class Bird_Form(ModelForm):
    class Meta:
        model = Bird
        fields = ['name', 'description', 'color', 'age']


class Feeding_Form(ModelForm):
    class Meta:
        model = Feeding
        fields = ['date', 'meal']