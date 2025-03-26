from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Places
from .serializers import PlacesSerializer

import json

@api_view(['GET'])
def get_places(request):
    if request.method == 'GET':
        places = Places.objects.all()

        serializer = PlacesSerializer(places, many=True)
        return Response(serializer.data)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_place_by_name(request, name):
    try:
        place = Places.objects.get(pk=name)
    except:
        
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    if request.method == 'GET':
        serializer = PlacesSerializer(place)
        return Response(serializer.data)