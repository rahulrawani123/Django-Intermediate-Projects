from django.shortcuts import render

# Create your views here.

def MyResume(request):
    return render(request,'home.html')
