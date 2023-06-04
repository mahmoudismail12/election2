from django.shortcuts import render
from django.views.generic.edit import FormMixin
# Create your views here.

from django.views.generic import ListView 
from camp.forms import Currentform
from camp.models import Campaign, Nominated

#########################################

def validcamp(request):
    valid =Campaign.objects.filter(current = True)
    return render(request,'voting/validcamp.html',{'valid':valid})

########################################
def vote(request,slug) :
    campaign= Campaign.objects.filter(slug=slug)    
    for campaign in campaign : 
        nomi = Nominated.objects.filter(campaign= campaign)
        return render(request,'voting/vote.html',{'nomi':nomi})
    
########################################

class Current(ListView,FormMixin) :
    model = Campaign
    form_class = Currentform
    template_name = 'voting/current.html'

    current = False
    def form_valid(self, form):
        self.current = True
        return super().form_valid(form)
########################################

class voting (ListView) :
    model = Nominated

    def get_queryset(self):
        id = self.id
        object
        return super().get_queryset()


