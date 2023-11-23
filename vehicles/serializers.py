from rest_framework import serializers
from .models import Vehicle


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

class VehicleDeepSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    car_make = serializers.CharField()


class VehicleCreateSerializer(serializers.Serializer):
    car_make = serializers.CharField(max_length=100)
    model = serializers.CharField(max_length=100)
    plate_num = serializers.CharField(max_length=10)
    price_day = serializers.DecimalField(max_digits=10, decimal_places=3)
    condition = serializers.CharField(max_length=8, required=False)

    def create(self, validated_data):
        #print(validated_data)
        return Vehicle.objects.create(
            **validated_data
        )

class VehicleUpdateSerializer(serializers.Serializer):
    car_make = serializers.CharField(max_length=100, required=False, write_only=True)
    model = serializers.CharField(max_length=100, required=False, write_only=True)
    plate_num = serializers.CharField(max_length=10, required=False, write_only=True)
    price_day = serializers.DecimalField(max_digits=10, required=False, decimal_places=3, write_only=True)
    condition = serializers.CharField(max_length=8, required=False, write_only=True)

    message = serializers.ReadOnlyField()

    def update(self, instance, validated_data):
        # instance -> obj que recibimos en la instancia del serializador
        # validate_data -> Body Request
        #print(instance.__dict__)
        instance.__dict__.update(**validated_data)
        instance.save()

        #print(instance.__dict__)
        #print(validated_data)
        obj = {
            'car_make': instance.car_make,
            'model': instance.model,
            'plate_num': instance.plate_num
        }

        validated_data['message'] = f'Vehículo: {obj} actualizado!'

        return validated_data