from django.urls import path 
from .views import  Current
from . import views
from django.views.generic import TemplateView
from .api_view import CampaignList , NominatedList,apivote , NominatedUpdate ,AddVoterId,currentcamp
app_name = 'camp'

urlpatterns = [
    path('', TemplateView.as_view(template_name="home.html"), name='home'),

    path('valid/',views.validcamp,name='validcamp'),
    path('vote/<slug:slug>',views.vote,name='vote'),
    path('current/',Current.as_view(),name='current'),


    #camp api 
    path('api/camplist',CampaignList.as_view(),name='campain_list_api'),
    path('api/current' , currentcamp , name='current_api'),
    #nominated api
    path('api/nomlist',NominatedList.as_view(),name='nom_list_api'),
    path('api/vote/<int:id>' , apivote , name='api_vote'),
    path('api/nomupdate/<int:pk>' , NominatedUpdate.as_view() , name = 'nom_update'),
    #voterid api
    path('api/addvoterid' , AddVoterId.as_view() , name='add_voterid'),

]   
