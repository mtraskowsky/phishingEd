from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def challenge_View(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "challenge.html", {})

def styles(request):
    return render(request, 'challenge.html', {})