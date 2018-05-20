from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def main(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if formis_valid():
            form.save()
            return redirect('articles:articlehomepage')
    else:
        form = UserCreationForm()
    return render(request,'accounts/main.html',{'form':form})
