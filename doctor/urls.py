from django.urls import path
from rest_framework import routers

from doctor import views
from doctor.viewsets import *

router = routers.DefaultRouter()
router.register('doctors', DoctorViewSet)

urlpatterns = router.urls + [
    path('doctors/<int:id>/phone/', views.DoctorPhoneCallAPIView.as_view(), name='predict'),
]

