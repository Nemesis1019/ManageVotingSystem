from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    ROLE_CHOICES = (
        ("ADMIN", 'Admin'),
        ("LIDER", 'Lider')
    )
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)


class Admin(models.Model):
    name = models.CharField(max_length=50,default="carlos")

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="admin_account")


class Lider(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50,default="carlos")
    last_name = models.CharField(max_length=50)
    number_phone = models.IntegerField()
    address= models.CharField(max_length=100,default="calle9")
    coordinates=models.CharField(max_length=100,null=True)
    profile_photo = models.ImageField(upload_to='pictures/',null=True, blank=True)
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="lider_account")
