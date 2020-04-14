from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from . import models
from . import serializers


class Incidents(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,) 
    
    queryset = models.Incidents.objects.all()
    serializer_class = serializers.IncidentsSerializer
