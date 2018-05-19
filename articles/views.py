from django.shortcuts import render
from .models import articles

def homepage(request):
    var = articles.objects.all().order_by("date")
    return render(request,'articles\homepage.html',{"key":var})

# Create your views here.
