from django.contrib import admin
from  . models import Campaign , VoterId  , Nominated
# Register your models here.
admin.site.register(Campaign)
admin.site.register(VoterId)
admin.site.register(Nominated)