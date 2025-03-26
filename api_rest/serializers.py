from rest_framework import serializers
from .models import Places

class PlacesSerializer(serializers.ModelSerializer):
    class Meta: 
        #o model
        model = Places
        #os campos que serao transformados em json (todos)
        fields = '__all__'
        #se eu quiser apenas campos especificos, é so colocar em uma lista
    