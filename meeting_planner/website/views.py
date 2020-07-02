from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from meetings.models import Meeting
# Create your views here.


def welcome(request):
    return render (request , "website/welcome.html" , {"meetings" : Meeting.objects.all()})


def date(request):
    context = {'some' : 'esraa'

    }
    return HttpResponse("this date is" + str(datetime.now()) , context)


def about(request):
    return HttpResponse("abouuut")

def ideas(request):
    return render(request, 'ideas.html')