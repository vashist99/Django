from django.shortcuts import render

def homepage(request):
    return render(request,'articles\homepage.html')

def about(request):
    return render(request,'articles\\about.html')    

# Create your views here.
