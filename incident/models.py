from __future__ import unicode_literals
from django.db import models
from incident.choices import *


class Incidents(models.Model):
    incident_id = models.AutoField(primary_key=True)
    machine_id = models.CharField(max_length = 100)        
    client_id = models.CharField(max_length = 100)        
    deployment_id = models.CharField(max_length = 100)        
    module = models.CharField(max_length = 100, null=True)        
    package = models.CharField(max_length = 100, null=True)        
    title = models.CharField(max_length = 100)
    category = models.CharField(max_length = 100, choices = CATEGORY, default = "Snapback")
    summary = models.CharField(max_length = 100)
    incident_detail = models.CharField(max_length = 1000, null=True)
    time = models.DateTimeField(auto_now_add=True)
    severity = models.CharField(max_length = 100, choices = SEVERITY, default = 'Low')
    priority = models.CharField(max_length = 100, choices = PRIORITY, default = 'Low')
    status = models.CharField(max_length = 100, choices = STATUS, default = 'Active')

    class Meta:
        verbose_name = 'incident'
        verbose_name_plural = 'incidents'

    def __str__(self):
        return '{}'.format(self.incident_id)
