from __future__ import unicode_literals
from django.db import models
from incident.choices import *
from ckeditor.fields import RichTextField
from django.utils.crypto import get_random_string
# from django.contrib.auth.models import User


class Incidents(models.Model):
    # incident_id = get_random_string
    author = models.ForeignKey('auth.User', null=True, editable=False, on_delete=models.CASCADE)
    machine_id = models.CharField(max_length = 100)        
    client_id = models.IntegerField(choices = CLIENTS, default='')
    deployment_id = models.CharField(max_length = 100)        
    module = models.CharField(max_length = 100, blank=True, null=True)        
    package = models.CharField(max_length = 100, blank=True, null=True)        
    title = models.CharField(max_length = 100)
    category = models.CharField(max_length = 100, choices = CATEGORY, default = "Snapback")
    summary = models.TextField(max_length = 100)
    incident_detail = RichTextField(verbose_name=('Details'),max_length= 1000)
    time = models.DateTimeField(auto_now_add=True)
    severity = models.CharField(max_length = 100, choices = SEVERITY, default = 'Low')
    priority = models.CharField(max_length = 100, choices = PRIORITY, default = 'Low')
    status = models.CharField(max_length = 100, choices = STATUS, default = 'Active')


    class Meta:
        verbose_name = 'incident'
        verbose_name_plural = 'incidents'


    def __str__(self):
        return '{}'.format(self.id)