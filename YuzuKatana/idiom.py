from django.shortcuts import render
from django.views.decorators import csrf
from .search import search

def idiom(request):
    ctx = {}
    if request.POST:
        ctx['result'] = search.search(request.POST)
 #       ctx['result'] = list(request.POST.values())
    return render(request, "idiom.html", ctx)