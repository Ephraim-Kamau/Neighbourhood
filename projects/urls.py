from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    url('^$',views.projects_today,name='projectsToday'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^new/profile$',views.new_profile,name='new_profile'),
    url(r'^new/business$',views.new_business,name='new_business'),
    url(r'^new/post',views.new_post,name='new_post'),
    url(r'^find_business/(\d+)',views.find_business,name = 'find_project'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)