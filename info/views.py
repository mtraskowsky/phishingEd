from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def info_View(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "info.html", {})