from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def eggs(request):
    return HttpResponse('Eggs are great!')

def proton(request):
    return HttpResponse("Proton is an element")

def count(request):
    fulltext = request.GET['fulltext']
    
    wordlist = fulltext.split()

    worddictrionary = {}

    for word in wordlist:
        if word in worddictrionary:
            #Increase
            worddictrionary[word] += 1
        else:
            #add to the dictionart
            worddictrionary[word] = 1
    
    sortedwords = sorted (worddictrionary.items(), key = operator.itemgetter(1), reverse= True)

    return render(request, 'count.html',{'fulltext':fulltext, 'count':len(wordlist), 'sortedwords':sortedwords})