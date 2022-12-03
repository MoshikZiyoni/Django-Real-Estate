from django.urls import include, path
from . import views
 
app_name = 'property'
urlpatterns = [
   path('searchproperty/', views.searchproperty, name = "searchproperty" ),
   path('homepage/', views.home , name = "home"),
   path('api/', views.property_api, name='api'),
   path('project/api/', views.project_api, name='projectapi'),
   path('result/', views.result , name = "result"),
   path('all-projects/', views.all_projects, name='all_projects'),
   path('tlv-apt/', views.telaviva, name='telaviva'),
   path('Ramat-gan-apt/', views.ramatgan, name='ramatgan'),
   path('Rishon-lezion-apt/', views.rishon, name='rishon'),
   path('<id>/', views.single_apt, name='single_apt'),
   path('projects/<id>/', views.single_project, name='single_project')
   
   
]


