from rest_framework import serializers
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

        return Rent.objects.create(**validated_data)
    

class RentUpdateSerializer(serializers.Serializer):
    date_start = serializers.DateTimeField(required=False)
    date_end = serializers.DateTimeField(required=False)
    #user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)
    vehicle = serializers.PrimaryKeyRelatedField(queryset=Vehicle.objects.all(), required=False)

    message = serializers.ReadOnlyField()

    def update(self, instance, validated_data):
        vehicle = validated_data['vehicle']
        duration_in_days = (validated_data['date_end'] - validated_data['date_start']).days

        total_pay = duration_in_days * vehicle.price_day
        validated_data['total_pay'] = total_pay

        vehicle.condition = 'rent'
        vehicle.save()

        instance.__dict__.update(**validated_data)
        instance.save()

        validated_data['message'] = f'Renta del cliente ha sido actualizada!'

        print(instance.__dict__)
        return validated_data
