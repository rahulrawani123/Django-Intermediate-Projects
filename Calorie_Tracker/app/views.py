from django.shortcuts import render

# Create your views here.


def Calorie(request):
    import requests
    import json
    
    if request.method=="POST":
        query=request.POST['query']
        api_url="https://api.api-ninjas.com/v1/nutrition?query="
        api_request=requests.get(api_url + query,headers={'X-Api-key':'9MzDx+sXHDqdV7p3o9iacg==DQOcmB9Jqr9kQ7wV'})
        try:
            api=json.loads(api_request.content)
            print(api_request.content)
        except Exception as e:
            api="oops"
            print(e)
        return render(request,'Home.html',{'api':api})
    
    return render(request,'Home.html',{'query':'enter a valid query'})

            
