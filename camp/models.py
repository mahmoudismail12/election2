
from django.utils import timezone
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
camp_choices=(
    ('S','Single'),
    ('M','Multiple'),

)
#########################################

class Campaign(models.Model):
    name = models.CharField(max_length=100)
    details = models.TextField(max_length=2000)
    image = models.ImageField(upload_to='campimges/',null=True,blank = True)
    starttime = models.DateTimeField(default=timezone.now)
    endtime = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(null=True  , blank=True,unique=True)
    camptype = models.CharField(choices=camp_choices,max_length=20,default='Single')
    current = models.BooleanField(default=False)

    def __str__(self):
        return self.name 

    def save (self ,*args,**kwargs):
        if not self.slug :
            self.slug = slugify(self.name)
        super(Campaign,self).save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('campaign:campaign_detail',kwargs={'slug' : self.slug})  
      
    

     
#########################################      

class VoterId(models.Model):
    campaign = models.ForeignKey(Campaign , related_name="campaign_voterid" , on_delete = models.CASCADE)
    voterid = models.IntegerField(default=0,unique=True)
    def __str__(self):
        return str(self.campaign)
    


#########################################

class Nominated(models.Model):
    campaign = models.ForeignKey(Campaign , related_name="campaign_nominated" , on_delete = models.CASCADE)
    name = models.CharField(max_length=100)
    details = models.TextField(max_length=2000)
    image = models.ImageField(upload_to='nominatedimage/',null=True,blank = True)
    votecount = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name