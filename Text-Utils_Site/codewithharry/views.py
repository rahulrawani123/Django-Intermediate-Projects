from django.shortcuts import HttpResponse,render

def Home(request):
    return render(request,'index2.html')


def Analyze(request):
    djtext = (request.POST.get('text','default')) 
    removepunc = (request.POST.get('removepunc','off'))
    capfirst = (request.POST.get('capfirst','off'))
    newlineremover = (request.POST.get('newlineremover','off'))
    Extraspaceremover = (request.POST.get('Extraspaceremover','off'))
    Char_count = (request.POST.get('Char_count','off'))
   
    if(removepunc!="on" and capfirst!="on" and newlineremover!="on" and Extraspaceremover!="on"):
        return HttpResponse("No checkbox is selected ....")
    
    if(removepunc=="on"):
        
        analyzed = ""
        removepunc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in removepunc:
                analyzed += char
    
        params={
            'purpose':'Remove Punctuations',
            'analyzed_text':analyzed
        }
        djtext=analyzed
       # return render (request,'analyzed.html',params)

    if(capfirst=="on"):
        analyzed=""
        for char in djtext :
            analyzed+=char.upper()
         
        params={
            'purpose':'Capitalized-All',
            'analyzed_text':analyzed
        }   
       # return render (request,'analyzed.html',params)
        djtext=analyzed   
    
    if(newlineremover=="on"):
        analyzed=""
        for char in djtext :
            if char!="\n" and char!='\r':
                
                analyzed+=char
         
        params={
            'purpose':'Newlineremoved',
            'analyzed_text':analyzed
        }   
        #return render (request,'analyzed.html',params)
        djtext=analyzed
    
    if(Extraspaceremover=="on"):
        analyzed=""
        for index , char in enumerate(djtext):
            if not (djtext[index]==" " and djtext[index+1]==" "):
                
                analyzed+=char
         
        params={
            'purpose':'Extraspaceremoved',
            'analyzed_text':analyzed
        }   
        #return render (request,'analyzed.html',params)
        djtext=analyzed
    
    if(Char_count=="on"):
        analyzed=0
        for char in djtext:
            analyzed+=1
         
        params={
            'purpose':'Character-count',
            'analyzed_text':analyzed
        }   
        
        djtext=analyzed
    
    else:
        
        return render (request,'analyzed.html',params)
        
              
    
    
    

def Capfirst(request):
    
    return HttpResponse('''<h1>Capfirst</h1> <div> <a href="http://127.0.0.1:8000/"> Back-to-Home </a>''')

def Newlineremove(request):
    return HttpResponse('''<h1>Newlineremove</h1> <div> <a href="http://127.0.0.1:8000/"> Back-to-Home </a>''')

def Spaceremove(request):
    return HttpResponse('''<h1>Spaceremove</h1> <div> <a href="http://127.0.0.1:8000/"> Back-to-Home </a>''')

def Charcount(request):
    return HttpResponse('''<h1>Charcount</h1> <div> <a href="http://127.0.0.1:8000/"> Back-to-Home </a>''')
    

