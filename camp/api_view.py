from django.shortcuts import get_object_or_404
from .models import Campaign ,Nominated,VoterId
from .serializers import CampaignSerializer , NominatedSerializer , VoterIdSerializer,NomUpdateSerializer
from rest_framework.generics import ListAPIView , RetrieveUpdateAPIView , CreateAPIView  ,UpdateAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication 


class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return




#Campign
@api_view(['GET'])
def camplist(request):
    all_camp=Campaign.objects.all()
    data = CampaignSerializer(all_camp , many=True,context={"request":request}).data
    return Response({'data':data})


@api_view(['GET'])
def currentcamp(request):
    valid =Campaign.objects.filter(current = True)
    data =  CampaignSerializer(valid , many = True,context={"request":request}).data
    return Response({'data':data})


#VoterId

class AddVoterId (CreateAPIView):
    serializer_class = VoterIdSerializer
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
@api_view(['GET'])
def voteridcheck(request,id):
    all_ids=VoterId.objects.filter(voterid=id)
    data = VoterIdSerializer(all_ids, many = True).data
    return Response({'data':data})





#Nominated 

@api_view(['GET'])
def nomlist(request):
    all_nom=Nominated.objects.all()
    data = NominatedSerializer(all_nom , many=True,context={"request":request}).data
    return Response({'data':data})

class NominatedUpdate(RetrieveUpdateAPIView):
    queryset = Nominated.objects.all()
    serializer_class = NomUpdateSerializer
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

@api_view(['GET'])
def apivote(request,id) :
    campaign= Campaign.objects.filter(id=id)
    for campaign in campaign : 
        nomi = Nominated.objects.filter(campaign= campaign)
        data =  NominatedSerializer(nomi , many = True,context={"request":request}).data
        return Response({'data':data})
    

    





