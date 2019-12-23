from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'myhome.html')

def count(request):
    fulltext = request.GET['fulltext']
    myword = fulltext.split()
    new_dict = {}
    for word in myword:
        if word in new_dict:
            new_dict[word]+=1
        else:
            new_dict[word]=1
    sortedwords = sorted(new_dict.items(),key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html',{'fulltext':fulltext,'number':len(myword),'rwords':sortedwords})

def about(request):
    return render(request, 'about.html')
