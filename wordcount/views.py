from django.http import HttpResponse
from django.shortcuts import  render
import operator


def homepage(request):
    return render(request,'home.html' )
def aboutus(request):
    return render(request,'about.html')
#def mike(request):
def count(request):
    fulltext = request.GET['fulltext']

    wordslist = fulltext.split()

    worddictionary = {}

    for word in wordslist:
       if word in worddictionary :
          #Increase
          worddictionary[word] +=1
       else :
         # add to the dicdditionary
          worddictionary[word]=1
    sortedword= sorted(worddictionary.items(),key=operator.itemgetter(1),reverse = True)



    #print(fulltext)
    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordslist),'sortedword':sortedword})
