from django.db import models

class Person(models.Model):
  # Personal Characteristics
  first_name = models.CharField(max_length=64)
  last_name = models.CharField(max_length=64, default="")
  age = models.CharField(max_length=2)
  email = models.CharField(max_length=64, default="")

  # Ride Characteristics
  origination_city = models.CharField(max_length=64)
  origination_state = models.CharField(max_length=64)
  destination_city = models.CharField(max_length=64)
  destination_state = models.CharField(max_length=2)
  vehicle_make = models.CharField(max_length=64, default="")
  vehicle_model = models.CharField(max_length=64, default="")
  vehicle_color = models.CharField(max_length=64, default="")
  is_regular = models.BooleanField(default=True) # Is regular or premium ride
  date = models.CharField(max_length=64, default="")
  time = models.CharField(max_length=64, default="")
  taking_passengers = models.BooleanField(default=False)
  seats_available = models.IntegerField(default=0)
