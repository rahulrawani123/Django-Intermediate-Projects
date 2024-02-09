from django.shortcuts import render
from .models import Image

# Create your views here.

def carlovers(request):
    import requests
    newdict={}
    new={}

    if request.method=="POST":
        
        name = request.POST['name']
        var = Image.objects.filter(Name=name.lower())
        for j in var :
            new=j
        api_url = 'https://api.api-ninjas.com/v1/cars?model={}'.format(name)
        response = requests.get(api_url, headers={'X-Api-Key': '9MzDx+sXHDqdV7p3o9iacg==DQOcmB9Jqr9kQ7wV'})
        if response.status_code == requests.codes.ok:
            print("ok")
            
        else:
            print("Error:", response.status_code, response.text)
        report=response.json()
        for i in report:
            newdict=i
        #print(newdict)

    return render(request,'home.html',{'newdict':newdict,'new':new})


