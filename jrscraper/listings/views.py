from django.shortcuts import render
from django.http import HttpResponse
from listings.search import Search
import json

def search(request):
    count   = request.GET.get("count")
    count   = 30 if count.isdigit() == False else count
    search  = Search()
    results = search.findAll(count)
    return render(request, "search.html", {"results": results})

def delete(request):
    id      = request.POST.get("id")
    search  = Search()
    response= json.dumps(search.delete(id))
    return HttpResponse(response, content_type="application/json")