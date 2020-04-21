from rest_framework import serializers
from . import models


class IncidentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Incidents
        fields = ('id', 'time', 'machine_id', 'client_id', 'deployment_id', 'module', 'package', 'title', 'category', 'summary', 'incident_detail', 'severity', 'priority', 'status')


    # def create(self, validated_data):
    #     inc_model = models.Incidents.objects.all()
    #     incident_list = inc_model[0]
    #     validated_data['incident_id'] = incident_list

    #     if validated_data.get('incident_list') is None:
    #         validated_data['incident_list'] = incident_list

    #     return super().create(validated_data)
