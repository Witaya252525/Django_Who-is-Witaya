from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def Home(request):
    return render (request ,'home/home.html')
 #   return HttpResponse (' <h1>Hi witaya</h1>' )