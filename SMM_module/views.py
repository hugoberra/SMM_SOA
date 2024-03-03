from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Municipality
from .serializers import MunicipalitySerializer

class MunicipalityListCreate(generics.ListCreateAPIView):
    queryset = Municipality.objects.all()
    serializer_class = MunicipalitySerializer

class MunicipalityRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Municipality.objects.all()
    serializer_class = MunicipalitySerializer
