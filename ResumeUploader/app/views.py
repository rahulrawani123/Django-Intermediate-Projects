from django.shortcuts import render,redirect
from .models import Resume

# Create your views here.

def ResumeMaker(request):
    if request.method=='POST':
        Name=request.POST['Name']
       
        Gender=request.POST['Gender']
        Locality=request.POST['Locality']
        City=request.POST['City']
        Pin=request.POST['Pin']
        State=request.POST['State']
        Mobile_No=request.POST['Mobile']
        Email=request.POST['Email']
        Job_City=request.POST['Job']
        Profile_Image=request.FILES.get('image')
        Resume.objects.create(Name=Name,Gender=Gender,Locality=Locality,City=City,Pin=Pin,State=State,Mobile_No=Mobile_No,Email=Email,Job_City=Job_City,Profile_Image=Profile_Image)
        
    return render(request,'Home.html')

def List(request):
    candidates=Resume.objects.all
    return render(request,"list.html",{"candidates":candidates})

def Candidate(request,pk):
    Details=Resume.objects.get(pk=pk)
    return render(request,"candidate.html",{"Details":Details})
