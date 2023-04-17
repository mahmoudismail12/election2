from django.urls import path 
from .views import CampaignList , CampaignDetail
from . import views

app_name = 'camp'

urlpatterns = [
    path('',CampaignList.as_view(), name='campaign_list'),
    path('<slug:slug>',CampaignDetail.as_view(),name='campaign_detail'),
    path('add/', views.CampADD.as_view(),name='camp_add'),
    path('<slug:slug>/edit',views.CampUpdate.as_view(),name='camp_update'),
]   