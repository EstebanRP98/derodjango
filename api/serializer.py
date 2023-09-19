from rest_framework import serializers
from .models import Cita, Venture


class VentureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venture
        fields = '__all__'


class CitaSerializer(serializers.ModelSerializer):
    venture = VentureSerializer()  # Agrega el campo venture

    class Meta:
        model = Cita
        fields = '__all__'
