from django.contrib import admin
from  . models import Campaign , VoterId  , Nominated
from django_summernote.admin import SummernoteModelAdmin 

class SomeModelAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'


# Register your models here.
admin.site.register(Campaign , SomeModelAdmin)
admin.site.register(VoterId)
admin.site.register(Nominated)