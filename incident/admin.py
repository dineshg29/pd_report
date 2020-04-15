from django.contrib import admin
from incident.models import Incidents


# Register your models here.

class incidentsAdmin(admin.ModelAdmin):
        list_display = ('incident_id', 'machine_id', 'client_id', 'deployment_id', 'title', 'severity', 'priority', 'status')


admin.site.register(Incidents, incidentsAdmin)
