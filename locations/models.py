from django.db import models


class Departament(models.Model):
    name = models.CharField(max_length=50)


class Municipality(models.Model):
    name = models.CharField(max_length=50)

    department = models.ForeignKey(Departament, on_delete=models.CASCADE)


class Votingbooth(models.Model):
    name = models.CharField(max_length=50)
    adress = models.CharField(max_length=100, null=False, default="r")
    coordinates = models.CharField(max_length=100, null=True)

    municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE, default=1)
