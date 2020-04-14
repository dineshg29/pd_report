from rest_framework import serializers
from . import models


class IncidentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Incidents
        fields = ('incident_id', 'time', 'machine_id', 'client_id', 'deployment_id', 'module', 'package', 'title', 'category', 'summary', 'incident_detail', 'severity', 'priority', 'status')