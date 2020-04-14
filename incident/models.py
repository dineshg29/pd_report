from django.db import models


class Incidents(models.Model):
    incident_id = models.AutoField(primary_key=True)
    machine_id = models.CharField(max_length = 100)        
    client_id = models.CharField(max_length = 100)        
    deployment_id = models.CharField(max_length = 100)        
    module = models.CharField(max_length = 100, null=True)        
    package = models.CharField(max_length = 100, null=True)        
    title = models.CharField(max_length = 100)


    class Category(models.TextChoices):
        SB = 'Snapback','Snapback',
        RS = 'Robot stopped', 'Robot stopped',
        AE = 'Audio error', 'Audio error',
        BP = 'Battery problem', 'Battery problem', 
        HE = 'Hardware error', 'Hardware error',
        HF = 'Heartbeat flicker', 'Heartbeat flicker',


    category = models.CharField( 
        max_length = 100, 
        choices = Category.choices, 
        default = "Snapback"
    )

    summary = models.CharField(max_length = 100)
    incident_detail = models.CharField(max_length = 1000, null=True)
    time = models.DateTimeField(auto_now_add=True)


    class Severity(models.TextChoices):
            LOW = 'Low', 'Low', 
            MED = 'Medium', 'Medium',
            CRI = 'Critical', 'Critical',

    severity = models.CharField( 
        max_length = 100, 
        choices = Severity.choices, 
        default = 'Low'
    )


    class Priority(models.TextChoices):
            LOW = 'Low', 'Low', 
            MED = 'Medium', 'Medium',
            HI = 'High', 'High',

    priority = models.CharField( 
        max_length = 100, 
        choices = Priority.choices, 
        default = 'Low'
    )


    class Status(models.TextChoices):
        ACT = 'Active', "Active"
        ACK = 'Acknowledged', "Acknowledged"
        RES = 'Resolved', "Resolved"

    status = models.CharField( 
        max_length = 100, 
        choices = Status.choices, 
        default = Status.ACT
    )