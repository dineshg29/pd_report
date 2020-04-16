from rest_framework import routers
from incident import views as incident_views

router = routers.DefaultRouter()
router.register(r'details', incident_views.Incidents)