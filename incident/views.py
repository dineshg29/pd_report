from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers


class Incidents(viewsets.ModelViewSet):
    queryset = models.Incidents.objects.all()
    serializer_class = serializers.IncidentsSerializer
