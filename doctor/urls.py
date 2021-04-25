from rest_framework import routers

from doctor.viewsets import *

router = routers.DefaultRouter()
router.register('doctors', DoctorViewSet)

urlpatterns = router.urls
