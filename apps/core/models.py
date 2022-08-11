from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Drone(models.Model):
    MODEL_CHOICES = (
        ('Lightweight', 'Lightweight'),
        ('Middleweight', 'Middleweight'),
        ('Cruiserweight', 'Cruiserweight'),
        ('Heavyweight', 'Heavyweight')
    )
    STATE_CHOICES = (
        ('IDLE', 'IDLE'),
        ('LOADING', 'LOADING'),
        ('LOADED', 'LOADED'),
        ('DELIVERING', 'DELIVERING'),
        ('DELIVERED', 'DELIVERED'),
        ('RETURNING', 'RETURNING'),
    )
    serial_number = models.CharField(primary_key=True, max_length=100)
    model = models.CharField(max_length=14, choices=MODEL_CHOICES)
    weight_limit = models.DecimalField(decimal_places=4, max_digits=7,
                                       validators=[MaxValueValidator(500), 
                                       MinValueValidator(0)])
    battery_percentage = models.IntegerField(validators=[
        MaxValueValidator(100), MinValueValidator(0)])
    state = models.CharField(max_length=11, choices=STATE_CHOICES)
