from rest_framework import serializers
from .models import Campaign , Nominated  ,VoterId
from django_filters.rest_framework import  FilterSet



class CampaignSerializer(serializers.ModelSerializer):
    class Meta :
        model = Campaign
        fields = "__all__"


class NominatedSerializer(serializers.ModelSerializer):
    class Meta :
        model = Nominated
        fields = "__all__"

class VoterIdSerializer(serializers.ModelSerializer):
    class Meta :
        model = VoterId
        fields = "__all__"