from django.shortcuts import render
from django.http import HttpResponse
from listings.search import Search
import pprint

def search(request):
    search  = Search()
    results = search.findAll()

    return render(request, "search.html", {
        "results": results
    })