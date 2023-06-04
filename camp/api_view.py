from .models import Campaign ,Nominated
from .serializers import CampaignSerializer , NominatedSerializer , VoterIdSerializer
from rest_framework.generics import ListAPIView , RetrieveUpdateAPIView , CreateAPIView  ,UpdateAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response





#Campign
class CampaignList(ListAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer

@api_view(['GET'])
def currentcamp(request):
    valid =Campaign.objects.filter(current = True)
    data =  CampaignSerializer(valid , many = True,context={"request":request}).data
    return Response({'data':data})


#VoterId
class AddVoterId (CreateAPIView):
    serializer_class = VoterIdSerializer





#Nominated 
class NominatedList(ListAPIView):
    queryset = Nominated.objects.all()
    serializer_class = NominatedSerializer

class NominatedUpdate(UpdateAPIView):
    queryset = Nominated.objects.all()
    serializer_class = NominatedSerializer

@api_view(['GET'])
def apivote(request,id) :
    campaign= Campaign.objects.filter(id=id)
    for campaign in campaign : 
        nomi = Nominated.objects.filter(campaign= campaign)
        data =  NominatedSerializer(nomi , many = True,context={"request":request}).data
        return Response({'data':data})
    

    





