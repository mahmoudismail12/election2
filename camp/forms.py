from django import forms
from camp.models import Campaign, Nominated



class Currentform(forms.ModelForm):
    class Meta :
        model = Campaign
        fields = ['current']