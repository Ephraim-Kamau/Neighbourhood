from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.projects_today,name='projectsToday'),
    url(r'^search/', views.search_results, name='search_results')


]