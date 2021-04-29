from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from doctor.models import DoctorStats


class DoctorPhoneCallAPIView(APIView):
    def get(self, request, *args, **kwargs):
        doctor_id = kwargs.get('id')
        doctor = DoctorStats.objects.filter(doctor_id=doctor_id).first()
        count = 0
        if doctor:
            count = doctor.no_of_phone_calls

        return JsonResponse({'no_of_phone_calls': count})

    def post(self, request, *args, **kwargs):
        doctor_id = kwargs.get('id')
        doctor = DoctorStats.objects.filter(doctor_id=doctor_id).first()
        if doctor:
            doctor.no_of_phone_calls += 1
            doctor.save()
        else:
            DoctorStats.objects.create(doctor_id=doctor_id, no_of_phone_calls=1)

        return Response()