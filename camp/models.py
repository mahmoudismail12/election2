from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class Campaign(models.Model):
    name = models.CharField(max_length=100)
    details = models.TextField(max_length=2000)
    starttime = models.DateTimeField(null=True)
    endtime = models.DateTimeField(null=True)
    slug = models.SlugField(null=True  , blank=True)
    def __str__(self):
        return self.name 


    def save (self , *args,**kwargs):
        if not self.slug :
            self.slug = slugify(self.name)
        super(Campaign,self).save(*args,**kwargs)


    def get_absolute_url(self):
       
        return reverse('campaign:campaign_detail',kwargs={'slug' : self.slug})   
        
class VoterId(models.Model):
    campaign = models.ForeignKey(Campaign , related_name="campaign_voterid" , on_delete = models.CASCADE)
    voterid = models.IntegerField(default=0,null=True)
    def __str__(self):
        return str(self.campaign)

class Nominated(models.Model):
    campaign = models.ForeignKey(Campaign , related_name="campaign_nominated" , on_delete = models.CASCADE)
    name = models.CharField(max_length=100)
    details = models.TextField(max_length=2000)
    image = models.ImageField(upload_to='nominatedimage/')
    votecount = models.IntegerField(default=0,null=True)
    

    def __str__(self):
        return self.name