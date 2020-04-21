from django.contrib import admin
from incident.models import Incidents


# Register your models here.

class incidentsAdmin(admin.ModelAdmin):
        list_display = ('id', 'machine_id', 'client_id', 'deployment_id', 'title','time', 'severity', 'priority', 'status')

        def save_model(self, request, obj, form, change):
                obj.author = request.user
                super().save_model(request, obj, form, change)

        #Using that queryset manager created before
        def get_queryset(self, request):
                qs = super().get_queryset(request)
                if request.user.is_superuser:
                        return qs
                return qs.filter(author=request.user)
                
admin.site.register(Incidents, incidentsAdmin)
