from django.http  import HttpResponse
import datetime as dt
from django.shortcuts import render,redirect
from .models import NeighbourHood,Profile,Businesses,Posts
from .forms import NewProfileForm,NewPostsForm,NewBusinessesForm



# Create your views here.

def projects_today(request):
    posts = Posts.objects.all()

    return render(request, 'today-projects.html', {"posts":posts}) 

def profile(request):
    current_user=request.user

    return render(request, 'profile.html', {"profile":profile,"current_user":current_user})

def new_profile(request):
    current_user=request.user

    if request.method=='POST':
        form=NewProfileForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)      
            post.profile = current_user
            post.save()
        return redirect("profile")
    else:
        form = NewProfileForm() 
    return render(request,'new_profile.html',{"form":form})

def new_business(request):
    current_user=request.user

    if request.method=='POST':
        form=NewBusinessesForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)      
            post.profile = current_user
            post.save()
        return redirect("projectsToday")
    else:
        form = NewBusinessesForm() 
    return render(request,'new_business.html',{"form":form})

def new_post(request):
    current_user=request.user

    if request.method=='POST':
        form=NewPostsForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)      
            post.profile = current_user
            post.save()
        return redirect("projectsToday")
    else:
        form = NewPostsForm() 
    return render(request,'new_post.html',{"form":form})    



def search_results(request):

    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        searched_business = Business.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"business": searched_business})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})    

  