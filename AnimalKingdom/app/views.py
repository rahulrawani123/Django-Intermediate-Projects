from django.shortcuts import render
from django.contrib import messages

# Create your views here.

def AnimalKingdom(request):
    if request.method=="POST":
        
        number1=request.POST['num1']
        number2=request.POST['num2']
        number3=request.POST['num3']
        number4=request.POST['num4']
        number5=request.POST['num5']
        number6=request.POST['num6']
        score=0
        if number1=="giraffe":
            score+=1
        score+=0
        if number2=="arctic whale":
            score+=1
        score+=0
        if number3=="8":
            score+=1
        score+=0
        if number4=="ostrich":
            score+=1
        score+=0
        if number5=="dove":
            score+=1
        score+=0
        if number6=="cheetah":
            score+=1
        score+=0
        messages.success(request,f'Your Score is {score}/6')
        
    return render(request,'Home.html')
