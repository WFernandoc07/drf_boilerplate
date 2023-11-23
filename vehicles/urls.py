from django.urls import path
from .views import VehicleView, VehicleGetById

urlpatterns = [
    path('', VehicleView.as_view(), name='vehicle_create'),
    path('<int:id>/', VehicleGetById.as_view(), name='read_update_delete')
]