from django.dispatch import receiver
from django.db.models.signals import pre_save,post_save

from .models import Votingbooth,Municipality,Departament
from locations.utils import get_coordinates,get_coordinates_and_location


@receiver(pre_save, sender=Votingbooth)
def set_coordenadas(sender, instance, **kwargs):
    if instance.adress:
        value= get_coordinates(instance.adress)
        instance.coordinates = f"{value}"
        
@receiver(pre_save, sender=Votingbooth)
def setdepartment(sender, instance, **kwargs):
    
        valor1,valor, valor3 = get_coordinates_and_location(instance.adress)
        department, _ = Departament.objects.get_or_create(name=valor3)
        instance.department = department
       
        
@receiver(pre_save, sender=Votingbooth)
def setmunicipality(sender, instance, **kwargs):
        
        valor1,valor2, valor3 = get_coordinates_and_location(instance.adress)
        department, _ = Departament.objects.get_or_create(name=valor3)
        municipality, created = Municipality.objects.get_or_create(name=valor2, department=department)
        instance.municipality = municipality
       

    