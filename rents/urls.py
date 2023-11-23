from rest_framework.urls import path
from .views import RentView, RentGetById

urlpatterns = [
    path('', RentView.as_view(), name='rent_create'),
    path('<int:id>/', RentGetById.as_view(), name='read_update_delete')
]