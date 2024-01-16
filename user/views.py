from django.shortcuts import render
from .forms import User

# Create your views here.
def register(request):
    form = User()
    return render(request,'register.html',{'form':form});