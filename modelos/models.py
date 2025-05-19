from django.db import models

# Create your models here.
class modelo(models.Model):
    Id_user = models.CharField(primary_key=True, max_length=50,auto_created=True)
    fristName = models.CharField(max_length=50,)
    lastName = models.CharField(max_length=50)
    yearOld = models.IntegerField(max_length=3)
#i do make axample por document of Django 
#handling  for primary key an d foreign key  on two models
class musician(models.Model):
    firts_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)
    
class album(models.Model):
    artist = models.ForeignKey(musician,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()     