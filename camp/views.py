from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView  , DetailView
from camp.models import Campaign



class CampaignList(ListView)  :
    model  =  Campaign

class CampaignDetail(DetailView)  : 
    model  =  Campaign