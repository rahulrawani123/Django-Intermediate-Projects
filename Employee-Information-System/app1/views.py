from django.shortcuts import render,redirect
from .forms import EmployeeForm
from .models import Employee
# Create your views here.
def home(request):
    form=EmployeeForm()
    if request.method=="POST":
        var=EmployeeForm(request.POST)
        var.save()
        var=EmployeeForm()
    data=Employee.objects.all()
    context={
        'form':form,
        'data':data,
    }
    return render(request,'app1/index.html',context)

def Delete(request,id):
    a=Employee.objects.get(pk=id)
    a.delete()
    return redirect('/' )

def update(request,id):
    if request.method=='POST':
        
        data=Employee.objects.get(pk=id)
        form=EmployeeForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
    else:
        data=Employee.objects.get(pk=id)
        form=EmployeeForm(instance=data)
    context={
        'form':form,
    }
    return render (request,'app1/update.html',context) 






