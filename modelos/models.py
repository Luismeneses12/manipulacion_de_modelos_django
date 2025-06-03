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
 # choices haldling 
class person(models.Model):
    Shirt_sizes={
        "S":"small",
        "M":"medium",
        "L":"large"
    }
    name = models.CharField(max_length=60)
    shirt_size= models.CharField(max_length=1,choices=Shirt_sizes)
 
 # also use choices in conise way 
 
class runner(models.Model):
    medalType = models.TextChoices("madalType","GOLD SILVER BRONZE")
    name = models.CharField(max_length=60)
    medal = models.CharField(blank=True,choices=medalType,max_length=10)
 
# crater to primary key  default  addn fil d dajango create new  for  if primary key is true form field   de name o  
class fruit(models.Model):
    name= models.CharField(max_length=100,primary_key=True)
    
 #  Automatic primary key fields 
class AutomatiPK (models.Model):
     id = models.BigAutoField(primary_key=True)
     firstName = models.CharField("person´s first name",max_length=30)
     
#relashape  class manyToOne
class ForeignKey(models.Model):
    fk =models.ForeignKey(AutomatiPK, on_delete=models.CASCADE)     
    seconMane= models.CharField(max_length=20)  
    
 #three example of d eforeign key in de cacadse soucer 
 
class Artist(models.Model):
     name= models.CharField(max_length=10)


class Album1(models.Model):
    artist = models.ForeignKey(Artist,on_delete=models.CASCADE)
            

class Song(models.Model):
    artist = models.ForeignKey(Artist,on_delete=models.CASCADE)
    album= models.ForeignKey(Album1,on_delete=models.RESTRICT)                       
    