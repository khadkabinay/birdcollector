from django.contrib import admin

# import your models here
from .models import Bird, Feeding

# Register your models here.
admin.site.register(Bird)
admin.site.register(Feeding)

