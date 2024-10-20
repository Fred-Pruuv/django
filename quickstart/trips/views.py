from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Trip
from .serializers import TripSerializer  # You need to create this serializer

# Existing view for the homepage
def index(request):
    return HttpResponse("Hello there! Welcome to the django-snowflake Quickstart!")

# Existing class-based view for the template rendering
class GrahamConselyeaView(generic.ListView):
    template_name = 'trips/trips-from-graham-conselyea.html'
    context_object_name = 'trip_list'

    def get_queryset(self):
        """Return the last 10 trips from the 'Graham Ave & Conselyea St' Citibike station."""
        return Trip.objects.filter(start_station_name='Graham Ave & Conselyea St')[:10]

# New API view to return JSON data
class TripListView(APIView):
    def get(self, request):
        trips = Trip.objects.filter(start_station_name='Graham Ave & Conselyea St')[:10]  # Fetch all trip objects or filter as needed
        serializer = TripSerializer(trips, many=True)  # Serialize the trip data
        return Response(serializer.data, status=status.HTTP_200_OK)