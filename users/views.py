from rest_framework.viewsets import generics
from rest_framework.response import Response
from rest_framework import status, permissions
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.http import JsonResponse
from .serializers import UserSerializer, UserCreateSerializer, UserUpdateSerializer
from .models import User
from .schemas import UserSchema


schema = UserSchema()

class UserView(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get', 'post']
    permission_classes = [permissions.IsAuthenticated]

    
    @swagger_auto_schema(
            operation_summary='Enpoint para listar usuarios',
            operation_description='Este servicio retorna la lista de usuarios',
            manual_parameters=schema.all()           
    )
    def get(self, request):
        query_params = request.query_params
        page = query_params.get('page')
        per_page = query_params.get('per_page')

        # filtro estático
        filters = {
            'is_staff': False, 'is_active':True
        }

        records = User.objects.filter(**filters).order_by('id')

        pagination = Paginator(records, per_page=per_page)
        # records = User.objects.all()

        nro_page = pagination.get_page(page)

        serializer = self.serializer_class(nro_page.object_list, many=True)
        return Response({
                'results': serializer.data,
                'pagination':{
                    'totalRecords': pagination.count,
                    'totalPages': pagination.num_pages,
                    'perPage': pagination.per_page,
                    'currentPage': nro_page.number
                }

            },status=status.HTTP_200_OK)

    @swagger_auto_schema(
            operation_summary='Enpoint para crear un usuario',
            operation_description='Este servicio permite crear un usuario',
            request_body=UserCreateSerializer
    )
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
class UserGetById(generics.GenericAPIView):
    serializer_class = UserSerializer
    http_method_names = ['get', 'patch', 'delete']
    

    @swagger_auto_schema(
            operation_summary='Enpoint para traer el usuario por ID',
            operation_description='Con este servicio obtenemos un usuario por su ID'
    )
    def get(self, request, id):
        # record = User.objects.filter(pk=id, is_active=True, 
        #                              is_staff=False).get()
        record = get_object_or_404(User, pk=id, is_active=True, is_staff=False)
        serializer = self.serializer_class(record)
        return Response(serializer.data, status.HTTP_200_OK)



    @swagger_auto_schema(
        operation_summary='Endpoint para actualizar un usuario por Id',
        operation_description='En este servicio actualizamos un usuario por el ID',
        request_body=UserUpdateSerializer
    )
    def patch(self, request, id):
        record = get_object_or_404(User, pk=id, is_active=True, is_staff=False)
        serializer = UserUpdateSerializer(record, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


    @swagger_auto_schema(
        operation_summary='Enpoint para inhabilitar un usuario por Id',
        operation_description='Con este servicio podemos ihabilitar un usuario por su Id'
    )
    def delete(self, _, id):
        record = get_object_or_404(User, pk=id, is_active=True, is_staff=False)
        record.is_active = False
        record.save()
        return Response(status.HTTP_204_NO_CONTENT)

