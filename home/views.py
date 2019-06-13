from django.shortcuts import render,redirect
from django.views.generic import ListView,DeleteView

# Create your views here.
def home(request):
    return render(request,'home.html')