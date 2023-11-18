from django.urls import path
from .views import UserView, UserGetById


urlpatterns = [
    path('', UserView.as_view(), name='list_create'),
    path('<int:id>/', UserGetById.as_view(), name='read_update_delete')
]