from django.shortcuts import render

from PMS.serializers import BuildingSerializers, RowsSerializers, FloorSerializers, ColoumnSerializers,VehicleSerializers,ParkingSerializers
from .models import Building, Rows, Floor, Coloumn, Vehicle,Parking
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from django.shortcuts import render
from .models import ParkingSlot, VehicleBooking

def dashboard(request):
    # Calculate the total, available, and booked parking slots
    total_slots = ParkingSlot.objects.count()
    available_slots = ParkingSlot.objects.filter(is_available=True).count()
    booked_slots = total_slots - available_slots
    
    # Fetch recent vehicle bookings (e.g., the last 5 bookings)
    recent_bookings = VehicleBooking.objects.all().order_by('-created_at')[:5]
    
    # Pass this data to the template
    context = {
        'total_slots': total_slots,
        'available_slots': available_slots,
        'booked_slots': booked_slots,
        'recent_bookings': recent_bookings,
    }
    
    return render(request, 'PMS/dashboard.html', context)

class BuildingView(generics.ListCreateAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializers

class FloorView(generics.ListCreateAPIView):
    queryset = Floor.objects.all()
    serializer_class = FloorSerializers

class RowsView(generics.ListCreateAPIView):
    queryset = Rows.objects.all()
    serializer_class = RowsSerializers

class ColoumnView(generics.ListCreateAPIView):
    queryset = Coloumn.objects.all()
    serializer_class = ColoumnSerializers

class VehicleView(generics.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializers
    
class ParkingView(generics.ListCreateAPIView):
    queryset = Parking.objects.all()
    serializer_class = ParkingSerializers