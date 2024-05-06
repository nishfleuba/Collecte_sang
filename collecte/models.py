from django.db import models

from django.contrib.auth.models import User

class Donneur(models.Model):
    id= models.AutoField(primary_key=True)
    nom=models.CharField(max_length=31)
    prenom=models.CharField(max_length=31)
    date_naissance=models.DateTimeField()
    groupe_sanguin=models.CharField(max_length=20)
    adresse=models.CharField(max_length=31)
    tel=models.IntegerField()
    def __str__(self):
        return f"{self.nom}  {self.prenom} afise group sanguin {self.groupe_sanguin}"




class Centre_Collecte(models.Model):
    id=models.AutoField(primary_key=True)
    nom=models.CharField(max_length=31)
    adresse=models.CharField(max_length=50)
    contact=models.IntegerField()
    def __str__(self):
        return f"{self.nom} dukorera {self.adresse}"

class Personnel_Medical(models.Model):
    id=models.AutoField(primary_key=True)
    personnel=models.OneToOneField(User,on_delete=models.CASCADE)
    specialite=models.CharField(max_length=40)
    collecte=models.OneToOneField(Centre_Collecte,null=False,on_delete=models.PROTECT)
    def __str__(self):
        return f"{self.nom}  {self.prenom} specialise en {self.specialite}"


class Don(models.Model):
    id=models.AutoField(primary_key=True)
    donneur=models.OneToOneField(Donneur,null=True,on_delete=models.CASCADE)
    created_by=models.OneToOneField(User,on_delete=models.CASCADE)
    collecte=models.OneToOneField(Centre_Collecte,null=False,on_delete=models.PROTECT)
    date_don=models.DateTimeField()
    quantite=models.IntegerField(editable=False,null=True)
    def __str__(self):
        return f"{self.donneur} yatanze {self.quantite}"
    
class Stock_Sang(models.Model):    
    id=models.AutoField(primary_key=True)
    don=models.OneToOneField(Don,on_delete=models.CASCADE,null=True,default=None)
    type_sang=models.CharField(max_length=31,null=False)
    quantite=models.IntegerField(null=False)
    date_reception=models.DateField(null=False)
    date_expiration=models.DateField(null=False)
    def __str__(self):
     return f"{self.type_sang} hasigaye {self.quantite}"



class Receveur(models.Model):
    id=models.AutoField(primary_key=True)
    nom=models.CharField(max_length=31)
    prenom=models.CharField(max_length=31)
    date_naissance=models.DateField()
    groupe_sanguin=models.CharField(max_length=35, null=True)
    def __str__(self):
        return f" {self.nom}  {self.prenom} afise {self.groupe_sanguin}"

class Transfusion(models.Model):
    Id=models.AutoField(primary_key=True)
    receveur=models.OneToOneField(Receveur,on_delete=models.CASCADE)
    date=models.DateField()
    quantite=models.IntegerField()
    stock=models.OneToOneField(Stock_Sang,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.receveur} akeneye {self.quantite}"
