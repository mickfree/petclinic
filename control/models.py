from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.
class Client(models.Model):
    name=models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone = models.IntegerField()
    
    def __str__(self):
        return self.name + " "+ self.last_name


class Pet(models.Model):
    SIZES = {
        "S": "Small",
        "M": "Medium",
        "H": "High",
    }
    name = models.CharField(max_length=50)
    race = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    size = models.CharField(max_length=1, choices=SIZES)
    client = models.ForeignKey(Client, on_delete=models.CASCADE,blank=True,null=True)
    
    def __str__(self):
        return "Nombre de la mascota: " + self.name + " Raza: "+ self.race + " Dueño: " + self.client.name
    
class Veterinarian(models.Model):
    SPECIALITY = {
        "Medicina Canina": "Medicina Canina",
        "Medicina Felina": "Medicina Felina",
        "Medicina Exótica": "Medicina Exótica",
    }
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    specialty = models.CharField(max_length=20,choices=SPECIALITY)
    
    def __str__(self):
        return f"{self.name} - {self.specialty}"
    
class ClinicalRecord(models.Model):
    RECORD = {
        "Consulta General": "Consulta General",
        "Operacion": "Operacion",
        "Control": "Control",
    }
    number_case = models.IntegerField(validators=[MinValueValidator(1000)], default=1000)
    record = models.CharField(max_length=50, choices=RECORD)
    patient = models.ForeignKey(Pet, on_delete=models.CASCADE,blank=True, null=True)
    veterinarian = models.ForeignKey(Veterinarian, on_delete=models.CASCADE, null=True) 
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.number_case}-{self.patient}-{self.veterinarian}-{self.date}"
    
    