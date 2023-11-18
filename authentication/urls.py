from django.urls import path
from .views import RegisterView, LoginView, RefreshTokenView, ResetPasswordView

urlpatterns = [
    path('signup/', RegisterView.as_view(), name='signup'),
    path('signin/', LoginView.as_view(), name='signin'),
    path('token/refresh', RefreshTokenView.as_view(), name='token_refresh'),
    path('password/reset', ResetPasswordView.as_view(), name='reset_password')
]