from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView  , DetailView
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from camp.models import Campaign



class CampaignList(ListView)  :
    model  =  Campaign

class CampaignDetail(DetailView)  : 
    model  =  Campaign

class CampUpdate(UpdateView) : 
    model = Campaign
    fields = ['name', 'details', 'starttime','endtime','slug','camptype']
    template_name = 'camp/campaign_edit.html'
    success_url = '/campaign'

class CampADD(CreateView) : 
    model = Campaign
    fields = ['name', 'details', 'starttime','endtime','slug','camptype']
    template_name = 'camp/campaign_add.html'
    success_url = '/campaign'

