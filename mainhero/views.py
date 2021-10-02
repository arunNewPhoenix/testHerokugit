from django.shortcuts import render

from .models import Person

# Create your views here.

def home(request):
    persons = Person.objects.all()
    return render(request,"index.html",{'persons':persons})
