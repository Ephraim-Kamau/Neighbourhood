from django.http  import HttpResponse
import datetime as dt
from django.shortcuts import render


# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def projects_today(request):
    date = dt.date.today()

    return render(request, 'all-projects/today-projects.html', {"date":date}) 

  