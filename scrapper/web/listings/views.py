from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing

def search(request):
    results = Listing.objects.all()
    print(results)
    return render(request, 'search.html', {
        'results': results
    })