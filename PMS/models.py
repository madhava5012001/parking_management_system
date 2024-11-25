from django.db import models
from account.models import User
from django.db import models
# Create your models here.

from django.db import models

class ParkingSlot(models.Model):
    slot_number = models.CharField(max_length=10)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Slot {self.slot_number}"

class VehicleBooking(models.Model):
    vehicle_number = models.CharField(max_length=20)
    parking_slot = models.ForeignKey(ParkingSlot, on_delete=models.CASCADE)
    time_slot = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=[('Booked', 'Booked'), ('Available', 'Available')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking for {self.vehicle_number}"

class Building(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,)
    building_name = models.CharField(max_length=50)
    address = models.TextField(max_length=100)
    total_floors = models.PositiveIntegerField(default=2)
    total_rows = models.PositiveIntegerField(default=10)
    total_coloumn = models.PositiveIntegerField()  

class Floor(models.Model):
    building_id = models.ForeignKey(Building,on_delete=models.CASCADE,)
    floor_name = models.CharField(max_length=40)

class Rows(models.Model):
    building_id = models.ForeignKey(Building,on_delete=models.CASCADE,)
    floor_id = models.ForeignKey(Floor,on_delete=models.CASCADE,)
    Row_name = models.CharField(max_length=50)

class Coloumn(models.Model):
    building_id = models.ForeignKey(Building,on_delete=models.CASCADE,)
    floor_id = models.ForeignKey(Floor,on_delete=models.CASCADE,)
    rows_id = models.ForeignKey(Rows,on_delete=models.CASCADE,)
    coloumn_name = models.CharField(max_length=40)

class Vehicle(models.Model):
    types = (
        ("two wheeler", 'two wheeler'),
        ("three wheeler", 'three wheeler'),
        ("Four wheeler", 'Four wheeler')
    )
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,)
    vechile_name = models.CharField(max_length=40)
    vechile_type = models.CharField(choices=types, max_length=30)
    vechile_no = models.CharField(max_length=40)

class Parking(models.Model):
    vehicle = models.ForeignKey(Vehicle,on_delete=models.CASCADE,)
    building = models.ForeignKey(Building,on_delete=models.CASCADE,)
    floor = models.ForeignKey(Floor,on_delete=models.CASCADE,)
    row = models.ForeignKey(Rows,on_delete=models.CASCADE,)
    coloumn = models.ForeignKey(Coloumn,on_delete=models.CASCADE,)