from django.shortcuts import render
from django.views.decorators import csrf
from .search import classics_index

def classics(request):
    ctx = {}

    if request.POST:
        ctx['result'] = classics_index.classic_index(request.POST['books'], int(request.POST['index']))
    return render(request, "classics.html", ctx)
