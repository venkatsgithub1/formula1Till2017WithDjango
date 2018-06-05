from django.db import models

class F1ChampionshipYears(models.Model):
    championship_year = models.PositiveIntegerField(unique=True)

class Country(models.Model):
    country = models.CharField(max_length=100, unique=True)

class Manufacturer(models.Model):
    manufacturer_name = models.TextField(unique=True)
    country = models.ForeignKey(Country, to_field="country", on_delete = models.CASCADE)

class DriverStandings(models.Model):
    driver_name = models.TextField()
    manufacturer = models.ForeignKey(Manufacturer, to_field="manufacturer_name", on_delete=models.CASCADE)
    driver_position = models.PositiveIntegerField()
    championship_year=models.ForeignKey(F1ChampionshipYears, to_field="championship_year", on_delete=models.CASCADE)
    country = models.ForeignKey(Country, to_field="country", on_delete = models.CASCADE)
    points = models.IntegerField()
