from django.shortcuts import render
from .models import Events
from django.utils import timezone
import datetime
# Create your views here.

def events(request):
    events = Events.objects.all()
    return render(request, 'events/events.html' , {'events': events})


# def events(request):
#     return render(request , "events.html" , {})
