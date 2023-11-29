from rest_framework import serializers
from django.shortcuts import get_object_or_404
from .models import Rent
from vehicles.models import Vehicle
from users.models import User

class RentSerializer(serializers.ModelSerializer):
    vehicle = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()
    class Meta:
        model = Rent
        fields = ['id', 'date_start', 'date_end', 'total_pay', 'user', 'vehicle']
        # fields = '__all__'
    
    
    def get_vehicle(self, obj):
        from vehicles.serializers import VehicleDeepSerializer
        # print(VehicleSerializer(obj.vehicle).data)
        return VehicleDeepSerializer(obj.vehicle).data
    def get_user(self, obj):
        from users.serializers import UserDeepSerializer
        return UserDeepSerializer(obj.user).data


class RentCreateSerializer(serializers.Serializer):
    date_start = serializers.DateTimeField()
    date_end = serializers.DateTimeField()
    total_pay = serializers.FloatField(read_only=True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    vehicle = serializers.PrimaryKeyRelatedField(queryset=Vehicle.objects.all())

    def create(self, validated_data):
        vehicle = validated_data['vehicle']
        duration_in_days = (validated_data['date_end'] - validated_data['date_start']).days

        total_pay = duration_in_days * vehicle.price_day
        validated_data['total_pay'] = total_pay

        vehicle.condition = 'rent'
        vehicle.save()
        print(validated_data)

        return Rent.objects.create(**validated_data)
    

class RentUpdateSerializer(serializers.Serializer):
    date_start = serializers.DateTimeField(required=False)
    date_end = serializers.DateTimeField(required=False)
    #user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)
    vehicle = serializers.PrimaryKeyRelatedField(queryset=Vehicle.objects.all(), required=False)

    message = serializers.ReadOnlyField()


    def update(self, instance, validated_data):
        # Trabajamos en Instance
        # Actualizamos a 'free' el vehiculo de 'instance'
        vehicle_instance_id = instance.__dict__['vehicle_id']
        record = Vehicle.objects.get(pk=vehicle_instance_id)
        record.condition = 'free'
        record.save()

        # Trabajamos en validate data
        # Instanciamos vehicle
        vehicle = validated_data['vehicle']
        # Calculamos total_pay
        date_end = validated_data['date_end']
        date_start = validated_data['date_start']
        duration_in_days = (date_end - date_start).days

        total_pay = duration_in_days * vehicle.price_day
        # Actualizamos total_pay
        validated_data['total_pay'] = total_pay

        # Actualizar la condición del vehiculo a 'rent'
        vehicle.condition = 'rent'
        vehicle.save()

        instance.__dict__.update(**validated_data)
        instance.save()


        validated_data['message'] = f'Renta del cliente ha sido actualizada!'    
        return validated_data
    
