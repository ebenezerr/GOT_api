from django.db import models


class Location(models.Model):
    place = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.place


class House(models.Model):
    name = models.CharField(max_length=100, unique=True)
    location = models.ForeignKey(Location, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"House {self.name}"


class Character(models.Model):
    name = models.CharField(max_length=100, unique=True)
    lastname = models.CharField(max_length=100)
    title = models.CharField(max_length=300)
    house = models.ForeignKey(House, null=True, on_delete=models.SET_NULL)
    portrayed_by = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.name} {self.lastname}"

