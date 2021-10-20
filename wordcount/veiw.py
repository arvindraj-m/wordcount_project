from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render (request,'home.html')
def count(request):
    fulltext=request.GET['fulltext']
    wordlis=fulltext.split()
    worddict={}
    for word in wordlis:
        if word in worddict:
            worddict[word]+=1
        else:
            worddict[word]=1
    return render(request,'count.html', {'fulltext':fulltext,'count':len(wordlis),'worddict':worddict.items()})
