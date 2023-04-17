from django import forms
from camp.models import Campaign



class CampForm(forms.ModelForm):
    class Meta :
        model = Campaign
        fields = '__all__'
        
