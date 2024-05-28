from django.db import models

from users.models import User
from locations.models import Votingbooth

# Create your models here.


class Voters(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=50)
    adress = models.CharField(max_length=50)
    number_phone = models.IntegerField()
    number_identification = models.IntegerField(unique=True)
    coordinates = models.CharField(max_length=50,null=True)
    
    votingbooth_id = models.ForeignKey(Votingbooth,on_delete=models.CASCADE, related_name="vootingbooth_id",default=1)
    user_id_created = models.ForeignKey(User, on_delete=models.CASCADE, related_name="voters_account",default=1)
