from django.forms import ModelForm
from .models import Bird


class Bird_Form(ModelForm):
    class Meta:
        model = Bird
        fields = ['name', 'description', 'color', 'age']