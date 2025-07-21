from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    a="""

       <h2> Home </h2><br>
       <a href="http://127.0.0.1:8000/Removepunc"><button>Removepunc</button></a><br>
       <a href="http://127.0.0.1:8000/capfirst"><button>capfirst</button></a><br>
       <a href="http://127.0.0.1:8000/newlineremove"><button>newlineremove</button></a><br>
       <a href="http://127.0.0.1:8000/spaceremove"><button>spaceremove</button></a><br>
       <a href="http://127.0.0.1:8000/charcount"><button>charcount</button></a><br>"""
    dictionary={'name':'Tanya','surname':'Goyal'}
    #return HttpResponse(a)
    return render(request,'index.html',dictionary)





def Removepunc(request):
    b=0
    
    dj_text = request.POST.get('text', 'default')
    Removepunctuation = request.POST.get('remove', 'off')
    fullcaps= request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    spaceremove=request.POST.get('spaceremove','off')
    counting=request.POST.get('counting','off')
    parameter={}
    if Removepunctuation == "on":
        p = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in dj_text:
            if char not in p:
                analyzed += char
        parameter = {'purpose': 'Removed Punctuation', 'analyzed_text': analyzed}
        dj_text=analyzed
        #return render(request, 'punctuation.html', parameter)
    if(fullcaps=="on"):
        analyzed="" 
        for char in dj_text:
            analyzed=analyzed+ char.upper()
        parameter={'purpose':'Convert to uppercase','analyzed_text':analyzed}
        dj_text=analyzed
        #return render(request,'punctuation.html',params)
    if(newlineremover=="on"):
        analyzed=""
        for char in dj_text:
            if char!="\n" and char!="\r":
                analyzed=analyzed+char
        parameter={'purpose':'Removed new line', 'analyzed_text':analyzed}
        dj_text=analyzed
        #return render(request,'punctuation.html',p)
    if(spaceremove=="on"):
        analyzed=""
        for index, char in enumerate(dj_text):
            if (dj_text[index]==" " and dj_text[index+1]==" "):
               pass
            else:
                analyzed+=char

        parameter={'purpose':'Remove extra space','analyzed_text':analyzed}
        dj_text=analyzed
       # return render(request,'punctuation.html',a)
    if(counting=="on"):
        b=len(dj_text)
        parameter['count']=f"character count:{b}"
       
        #return render(request,'punctuation.html',c)
    if(Removepunctuation!="on" and fullcaps!="on" and newlineremover!="on" and spaceremove!="on" and counting!="on"):
        return HttpResponse("Error")
    
    return render(request,'punctuation.html',parameter)

