from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Places
from .serializers import PlacesSerializer

import json

@api_view(['GET'])
def get_places(request):
    places = Places.objects.all()
    serializer = PlacesSerializer(places, many=True) #param many pois é u queryset
    return Response(serializer.data)

@api_view(['GET'])
def get_place_by_name(request, place_name):
    place = get_object_or_404(Places, name=place_name)
    serializer = PlacesSerializer(place)
    return Response(serializer.data)

@api_view(['POST'])
def create_place(request):
    serializer = PlacesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def edit_place(request, place_name):
    try:
        place_updated = Places.objects.get(pk=place_name)
    except Places.DoesNotExist:
            return Response({"error": "Lugar não encontrado"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = PlacesSerializer(place_updated, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    return Response(status=status.HTTP_400_BAD_REQUEST)
