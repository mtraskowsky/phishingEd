"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path

from listView.views import list_View
from info.views import info_View
from challenge.views import challenge_View

urlpatterns = [
    path('', list_View.as_view(), name='home'),
    path('info/', info_View, name='info'),
    path('challenge/', challenge_View, name='challenge'),
    path('admin/', admin.site.urls),
    #url(r'^https://blogs.k-state.edu/scams/', include('wordpress.urls')),
]
