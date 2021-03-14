from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView # to use class based views
# ListView allows us to list a query set
# DetailView makes a request to the database for us
from .models import Post

# Create your views here.
#def list_View(*args, **kwargs):
#    return HttpResponse("<h1>hello world</h1>")

#when using templates for home.html
# https://www.youtube.com/watch?v=F5mRW0jo-U4   at  1:10
#def list_View(request, *args, **kwargs):
#    return render(request, "list.html", {})

# to use class based views
# https://www.youtube.com/watch?v=CnaB4Nb0-R8 3:40
class list_View(ListView):
    model = Post
    template_name = 'list.html'
    ordering = ['-date']