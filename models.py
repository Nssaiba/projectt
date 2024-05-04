from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Offre(models.Model):
    id = models.BigAutoField(primary_key=True)
    nameP= models.CharField(max_length=100,blank=False,null=False)
    type=models.CharField(max_length=100,blank=False,null=False)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    description=models.TextField()
    date=models.DateField()
    image= models.ImageField(upload_to='offer_images/')
    date_added = models.DateTimeField(default=timezone.now)

def __str__(self):
    return self.name

class Evenements(models.Model):
    id = models.BigAutoField(primary_key=True)
    lieu=models.CharField(max_length=100,blank=False,null=False)
    categorie=models.CharField(max_length=100,blank=False,null=False)
    date=models.DateField()
    time = models.TimeField() 
    price=models.DecimalField(max_digits=10, decimal_places=2)
    description=models.TextField()
    image= models.ImageField(upload_to='event_images/')

def __str__(self):
        return self.lieu   

class Client(models.Model):
    id = models.BigAutoField(primary_key=True)
    Nom=models.CharField(max_length=100,blank=False,null=False)
    Prenom=models.CharField(max_length=100,blank=False,null=False)
    tel=models.CharField(max_length=10,blank=False,null=False)
    email=models.CharField(max_length=100,blank=False,null=False)
    password=models.CharField(max_length=100,blank=False,null=False)
    image = models.ImageField(upload_to='Client_images/', default='default.jpg')
   

def __str__(self):
        return self.Nom   

class Destination(models.Model):
    id = models.BigAutoField(primary_key=True)
    lieu=models.CharField(max_length=100,blank=False,null=False)
    categorie=models.CharField(max_length=100,blank=False,null=False)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    description=models.TextField()
    image= models.ImageField(upload_to='Destination_images/')

def __str__(self):
        return self.lieu    


# Create your models here.
# class Chat(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     message = models.TextField()
#     response = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f'{self.user.username}: {self.message}'
    
class Commentaire(models.Model):
    id = models.BigAutoField(primary_key=True)
    email=models.CharField(max_length=100,blank=False,null=False)
    comment=models.TextField()

def __str__(self):
        return self.email      

class Chat(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, blank=True)
    message = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username if self.user else "Anonymous User"}: {self.message}'

class Admins(models.Model):
    id = models.BigAutoField(primary_key=True)
    
    email=models.CharField(max_length=100,blank=False,null=False)
    password=models.CharField(max_length=100,blank=False,null=False)
    
   

def __str__(self):
        return self.email 
