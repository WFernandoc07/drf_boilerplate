from rest_framework.viewsets import generics
from rest_framework.response import Response
from rest_framework import status, permissions
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from .models import Rent
from .serializers import RentSerializer, RentCreateSerializer, RentUpdateSerializer
from .schemas import RentSchema

schema = RentSchema()

class RentView(generics.GenericAPIView):
    queryset = Rent.objects.all()
    serializer_class = RentSerializer
    http_method_names = ['get', 'post']
    # permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_summary='Endpoint para listar Rentas de Vehículos',
        operation_description='Con este servicio listamos las rentas de los vehículos',
        manual_parameters=schema.all()
    )
    def get(self, request):
        query_params = request.query_params
        page = query_params.get('page')
        per_page = query_params.get('per_page')

        records = Rent.objects.all()

        pagination = Paginator(records, per_page=per_page)

        num_page = pagination.get_page(page)

        #serializer = self.serializer_class(records, many=True)
        serializer = self.serializer_class(num_page.object_list, many=True)

        #return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({
            'results': serializer.data,
            'pagination': {
                'totalRecords': pagination.count,
                'totalPages': pagination.num_pages,
                'perPage': pagination.per_page,
                'currentPage': num_page.number
            }
        }, status=status.HTTP_200_OK)

    @swagger_auto_schema(
            operation_summary='Endpoint para registrar Rentas de Vehículos',
            operation_description='Con este servicio registramos la Rentas de los vehículos',
            request_body=RentCreateSerializer
    )    
    def post(self, request):
        serializer = RentCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class RentGetById(generics.GenericAPIView):
    serializer_class = RentSerializer
    http_method_names = ['get', 'patch', 'delete']
    # permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
            operation_summary='Enpoint para obtener una Renta por Id',
            operation_description='Con este servicio obtenemos una Renta por su Id'
    )
    def get(self, _, id):
        record = get_object_or_404(Rent, pk=id)
        serializer = self.serializer_class(record)
        return Response(serializer.data, status=status.HTTP_200_OK)


    @swagger_auto_schema(
            operation_summary='Enpoint para actualizar una Renta por Id',
            operation_description='Con este servicio actualizamos una Renta por su Id'
    )
    def patch(self, request, id):
        record = get_object_or_404(Rent, pk=id)
        serializer = RentUpdateSerializer(record, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


    @swagger_auto_schema(
            operation_summary='Enpoint en Construcción',
            operation_description='Endpoint en construcción'
    )
    def delete(self, _, id):
        return Response(status=status.HTTP_503_SERVICE_UNAVAILABLE)