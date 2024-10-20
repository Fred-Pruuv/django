# trips/serializers.py

from rest_framework import serializers
from .models import Trip

class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'  # Include all fields or specify which fields like ['field1', 'field2']
