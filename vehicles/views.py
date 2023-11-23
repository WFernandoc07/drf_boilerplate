from rest_framework.viewsets import generics
from rest_framework.response import Response
from rest_framework import status, permissions
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from .serializers import VehicleSerializer, VehicleCreateSerializer, VehicleUpdateSerializer
from .models import Vehicle
from .schemas import VehicleSchema

schema = VehicleSchema()


class VehicleView(generics.GenericAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    http_method_names = ['get', 'post']
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
            operation_summary='Endpoint para listar Vehículos',
            operation_description='Con este servicio listamos los Vehículos',
            manual_parameters=schema.all()
    )
    def get(self, request):
        query_params = request.query_params
        page = query_params.get('page')
        per_page = query_params.get('per_page')

        records = Vehicle.objects.all().order_by('id')

        pagination = Paginator(records, per_page=per_page)

        num_page = pagination.get_page(page)
        

        #filtro estático
        serializer = self.serializer_class(num_page.object_list, many=True)
        
        return Response({
                'results': serializer.data,
                'pagination':{
                    'totalRecords': pagination.count,
                    'totalPages': pagination.num_pages,
                    'perPage': pagination.per_page,
                    'currentPage': num_page.number
                }
            },status=status.HTTP_200_OK)
    
    
    @swagger_auto_schema(
            operation_summary='Endpoint para registrar Vehículos',
            operation_description='Con este servicio registramos los Vehículos',
            request_body=VehicleCreateSerializer
    )
    def post(self, request):
        # serializer = VehicleCreateSerializer
        serializer = VehicleCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class VehicleGetById(generics.GenericAPIView):
    serializer_class = VehicleSerializer
    http_method_names = ['get', 'patch', 'delete']
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
            operation_summary='Endpoint para obtener un Vehículo por el Id',
            operation_description='Con este servicio obtenemos un vehículo por el Id',
    )
    def get(self, request, id):
        record = get_object_or_404(Vehicle, pk=id)
        serializer = self.serializer_class(record)
        return Response(serializer.data, status=status.HTTP_200_OK)


    @swagger_auto_schema(
            operation_summary='Endpoint para actualizar un Vehículo por el Id',
            operation_description='Con este servicio actualizamos un vehículo por el Id',
            request_body=VehicleUpdateSerializer
    )
    def patch(self, request, id):
        record = get_object_or_404(Vehicle, pk=id)
        serializer = VehicleUpdateSerializer(record, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
            operation_summary='Endpoint para eliminar un Vehículo por el Id',
            operation_description='Con este servicio eliminar un vehículo por el Id'
    )
    def delete(self, _, id):
        # El vehículo no debe estar rentado
        record = get_object_or_404(Vehicle, pk=id)
        record.condition = 'inactive'
        record.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
