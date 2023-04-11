from django.urls import path 
from .views import CampaignList , CampaignDetail


app_name = 'camp'

urlpatterns = [
    path('',CampaignList.as_view(), name='campaign_list'),
    path('<slug:slug>',CampaignDetail.as_view(),name='campaign_detail')
]   