from django.db import models
from datetime import date
from django.urls import reverse

# Create your models here.


# A tuple of 2-tuples
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

class Bird(models.Model):
    name = models.CharField(max_length=100)
    description  = models.TextField(max_length=300)
    color = models.CharField(max_length=100)
    age = models.IntegerField()

    def fed_for_today(self):
        return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)


    def __str__(self):
        return self.name



# Add new Feeding model below Bird model
class Feeding(models.Model):
    date = models.DateField('feeding date')
    meal = models.CharField(
    max_length=1,
    # add the 'choices' field option
    choices=MEALS,
    # set the default value for meal to be 'B'
    default=MEALS[0][0]
  )

    # Create a Bird_id FK
    bird = models.ForeignKey(Bird, on_delete=models.CASCADE)

    def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.get_meal_display()} on {self.date}"


    class Meta:
        ordering = ['-date']


