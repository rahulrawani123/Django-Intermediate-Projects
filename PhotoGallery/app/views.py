from django.shortcuts import render,redirect
from .models import Category,Photos
# Create your views here.

def gallery(request):
    category=request.GET.get('Category')
    if category == None:
        photo=Photos.objects.all()
    else:
        photo=Photos.objects.filter(Category__Name__contains=category)
    
    Categories=Category.objects.all()
    
    context={
        'Categories':Categories,'photos':photo,
    }
    return render(request,'photos/gallery.html',context)

def view(request,pk):
    photos=Photos.objects.get(id=pk)
    return render(request,'photos/view.html',{'photos':photos})

def add(request):
    Categories=Category.objects.all()
    
    if request.method=='POST':
        data=request.POST
        image=request.FILES.get('image')
        
        
        if data['categor'] != 'none':
            cate = Category.objects.get(id=data['categor'])
        elif data['category_new'] !='':
            cate, created=Category.objects.get_or_create(Name=data['category_new'])
        else:
            cate=None
            
        photo=Photos.objects.create(
            Category=cate,
            Description=data['description'],
            image=image,
        )
        
        return redirect('gallery') 
    context={
        'Categories':Categories
    }
    return render(request,'photos/add.html',context)

