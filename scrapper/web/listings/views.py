from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#class search:
#    pass

def search(request):
    return render(request, 'listings/templates/search.html', {

    })