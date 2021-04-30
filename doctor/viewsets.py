import math

from rest_framework import viewsets, status
from rest_framework.response import Response

from doctor.distance import sort_doctors_by_distance
from doctor.serializers import *


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

    @staticmethod
    def add_experience(experiences, doctor_id):
        for experience in experiences:
            Experience.objects.create(
                doctor_id=doctor_id,
                hospital_name=experience.get('hospital_name'),
                position=experience.get('position'),
                experience=experience.get('experience'),
            )

    @staticmethod
    def add_education(education_list, doctor_id):
        for degree in education_list:
            Education.objects.create(
                doctor_id=doctor_id,
                degree=degree.get('degree'),
                university_name=degree.get('university_name'),
            )

    @staticmethod
    def truncate(f, n):
        res = math.trunc(f * 10 ** n) / 10 ** n
        return int(res) if n == 0 else res

    def create(self, request, *args, **kwargs):
        serializer_data = request.data
        lat = serializer_data.get('lat')
        long = serializer_data.get('long')

        if not (lat or long):
            lat, long = request.ipinfo.loc.split(',')
            serializer_data['lat'] = lat
            serializer_data['long'] = long

        experience_list = serializer_data.get('experience')
        education_list = serializer_data.get('education')
        serializer = self.get_serializer(data=serializer_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        doctor_id = serializer.data['id']
        self.add_experience(experience_list, doctor_id)
        self.add_education(education_list, doctor_id)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def list(self, request, *args, **kwargs):
        source_lat = request.query_params.get('source_lat')
        source_lon = request.query_params.get('source_lon')

        if not (source_lat or source_lon):
            source_lat, source_lon = request.ipinfo.loc.split(',')

        print(f'Source Latitude: {source_lat}; Source Longitude: {source_lon}')
        print(f'IP: {request.ipinfo.ip}')

        precision_level = request.data.get('precision_level', 0)

        search_lat = self.truncate(float(source_lat), precision_level)
        search_lon = self.truncate(float(source_lon), precision_level)

        nearby_doctors = Doctor.objects.filter(
            lat__startswith=search_lat,
            long__startswith=search_lon,
            is_active=True,
        ).values()

        doctors = sort_doctors_by_distance(nearby_doctors, (source_lat, source_lon))

        return Response(doctors)

