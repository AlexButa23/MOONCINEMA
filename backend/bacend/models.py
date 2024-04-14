from django.db import models

class film(models.Model):
    nume=models.CharField(max_length=50)
    imagine=models.CharField(max_length=50)
    trailer=models.URLField(max_length=200)
    gen=models.CharField(max_length=50)
    descriere=models.TextField()
    timp=models.CharField(max_length=50)
    an=models.CharField(max_length=50)
    locuri=models.IntegerField()
    
    def __str__(self):
         return self.nume + " - " + self.an
    class Meta:
         verbose_name_plural= "1. Filme"
    
class rezervare(models.Model):
    prenume=models.CharField(max_length=50,default="")
    nume_de_familie=models.CharField(max_length=50,default="")
    numar_card=models.CharField(max_length=100,default="")
    data_expirare_card=models.CharField(max_length=50,default="")
    cvv2=models.CharField(max_length=50,default="")
    email=models.EmailField(max_length=100,default="")
    locuri=models.CharField(max_length=1550)
    film=models.CharField(max_length=50)
    tip=models.CharField(max_length=50)
    data=models.CharField(max_length=50)

    def __str__(self):
         return self.tip+" - "+self.nume_de_familie+" "+""+self.prenume
    class Meta:
         verbose_name_plural= "2. Rezervări/Cumpărări"
     
class recomandari(models.Model):
    prenume=models.CharField(max_length=1550)
    nume_de_familie=models.CharField(max_length=1550)
    email=models.CharField(max_length=1550)
    subiect=models.CharField(max_length=1550)

    def __str__(self):
         return "Recomandare de la " + self.prenume + " " + self.nume_de_familie
    class Meta:
         verbose_name_plural= "3. Recomandări"
   

# Create your models here.
