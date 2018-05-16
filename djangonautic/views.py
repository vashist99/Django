from django.http import HttpResponse

def homepage(request):
    return HttpResponse('hello world!')

def about(request):
    return HttpResponse('this is the about page')
