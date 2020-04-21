from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
from incident.permissions import *


class Incidents(viewsets.ModelViewSet):
    queryset = models.Incidents.objects.all()
    serializer_class = serializers.IncidentsSerializer

    def get_permissions(self):
            self.permission_classes = [IsSuperUser]

            if self.action == 'retrieve':
                self.permission_classes = [IsOwner]

            return super(self.__class__, self).get_permissions()