from django.urls import path
from .views import BuildingView, RowsView, FloorView, ColoumnView, VehicleView,ParkingView
from django.urls import path
from . import views
urlpatterns = [
    path("building/", BuildingView.as_view(), name = "building"),
    path("floor/", FloorView.as_view(), name = "floor"),
    path("rows/", RowsView.as_view(), name = "rows"),
    path("coloumn/", ColoumnView.as_view(), name = "coloumn"),
    path('vehicle/', VehicleView.as_view()),
    path('parking/entry',ParkingView.as_view()),
    path('dashboard/', views.dashboard, name='dashboard'),
]