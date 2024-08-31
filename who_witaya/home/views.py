from django.shortcuts import render
from django.http import HttpResponse
from .models import ContactMessage
# Create your views here.


def Home(request):
    return render(request, 'home/home.html')


def Service(request):
    return render(request, 'home/service.html')


def Contact(request):

    context = {}
    if request.method == 'POST':
        data = request.POST.copy()
        title = data.get('title')
        email = data.get('email')
        detail = data.get('detail')

        print(title, email, detail)
        if email == '' or title == '' :
            context[ 'status'] = 'alert'
            return render(request, 'home/contact.html' ,context)

        # add data into database
        new = ContactMessage()
        new.title = title
        new.email = email
        new.detail = detail
        new.save()
        context[ 'status'] = 'sucess'

    return render(request, 'home/contact.html' ,context)

 #   return HttpResponse (' <h1>Hi witaya</h1>' )
