from django.dispatch import receiver
from django.db.models.signals import pre_save

from .models import Lider
from locations.utils import get_coordinates


@receiver(pre_save, sender=Lider)
def set_coordenadas(sender, instance, **kwargs):
    if instance.address:
        value = get_coordinates(instance.address)
        instance.coordinates = f"{value}"