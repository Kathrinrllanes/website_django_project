from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html', {'ejemploetiqueta': 'This is me'})

def about(request):
    return render(request, 'about.html')


def count(request):
    fulltext = request.GET['fulltext']
    words = fulltext.split()
    worddictionary = {}

    for word in words:
        if word in worddictionary:
            #Increase
            worddictionary[word] +=1
        else:
            worddictionary[word] = 1

    #ordenar un dictionary
    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(words), 'sortedwords':sortedwords })

def eggs(request):
    return HttpResponse('<h1>The eggs are great</h1>')


