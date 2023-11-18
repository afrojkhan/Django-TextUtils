# I have create this file 
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):

#Get the text

    djtext=request.POST.get('text','default')

#check checkbox values
    
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
   
    
#check which box is on    

    if removepunc == "on":
        punctuation='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuation:
                analyzed=analyzed+char  
        param={'purpose':'Remove_Puntuation','analyzed_text':analyzed}
        djtext=analyzed
      
    if fullcaps=="on":
        analyzed=''
        for char in djtext:
             analyzed=analyzed+char.upper()

        param={'purpose':'extra space remover','analyzed_text':analyzed}
        djtext=analyzed
       
    if extraspaceremover == "on":
        analyzed=''
        for index,char in enumerate(djtext):
             if not(djtext[index] == " " and djtext[index+1]==" "):
               
                analyzed=analyzed+char

        param={'purpose':'remove new lines','analyzed_text':analyzed}
        djtext=analyzed
      
    if newlineremover == "on":
        analyzed=''
        for char in djtext:
             if char !="\n" and char != "\r":
                 
                analyzed=analyzed+char
            
        param={'purpose':'remove new lines','analyzed_text':analyzed}
        
    if removepunc!="on" and fullcaps !="on" and newlineremover!="on" and extraspaceremover!="on":
        return HttpResponse("Please select theo peration")


    return render(request,'analyze.html',param)
