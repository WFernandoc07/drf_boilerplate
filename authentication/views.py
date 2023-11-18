from rest_framework.request import Request
from rest_framework.viewsets import generics
from rest_framework.response import Response
from rest_framework import status, permissions
from drf_yasg.utils import swagger_auto_schema
from rest_framework_simplejwt.views import TokenViewBase
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import RegisterSerializer, LoginSerializer, ResetPasswordSerializer


# Registro - POST -> 201
class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    http_method_names = ['post']

    @swagger_auto_schema (
            operation_summary='Endpoint para registrar un usuario',
            operation_description='En este servicio podria se podrá crear un nuevo usuario',
            security=[]
    )
    def post(self, request):
        # Instancia el serializador con los datos de body request
        serializer = self.serializer_class(data=request.data)

        # Iniciamos la validación del serializer
        serializer.is_valid(raise_exception=True)
        # Ejecutamos la acción
        serializer.save()
        # Retornamos la respuesta
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# Login - POST -> 200
class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    http_method_names = ['post']

    @swagger_auto_schema(
        operation_summary='Endpoint para logearse',
        operation_description='Con este servicio puesdes logearte con tu usuario y contraseña',
        security=[]
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# Resfresh Token - POST -> 200
class RefreshTokenView(TokenViewBase):
    serializer_class = TokenRefreshSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    @swagger_auto_schema (
            operation_summary='Endpoint para generar un nuevo acces__token',
            operation_description='Con este sevicio se genera un nuevo access_token desde el refresh token'
    )
    def post(self, request):
        return super().post(request)

#Reinicio de contraseña - POST -> 
class ResetPasswordView(generics.GenericAPIView):
    serializer_class = ResetPasswordSerializer

    @swagger_auto_schema(
            operation_summary='Enpoint para resetear la contraseña',
            operation_description='Con este servicio podemos resetear la contraseña',
            security=[]
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
