from django.dispatch import receiver
from django.db.models.signals import pre_save

from .models import Voters
from locations.utils import get_coordinates


@receiver(pre_save, sender=Voters)
def set_coordenadas(sender, instance, **kwargs):
    if instance.adress:
        value = get_coordinates(instance.adress)
        instance.coordinates = f"{value}"
