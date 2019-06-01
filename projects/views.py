from django.http  import HttpResponse
import datetime as dt
from django.shortcuts import render
from .models import NeighbourHood,Profile,Businesses,Posts


# Create your views here.

def projects_today(request):
    posts = Posts.objects.all()

    return render(request, 'all-projects/today-projects.html', {"posts":posts}) 


def search_results(request):

    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        searched_business = Business.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-projects/search.html',{"message":message,"business": searched_business})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-news/search.html',{"message":message})    

  