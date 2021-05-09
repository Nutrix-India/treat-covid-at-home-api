import requests

from app.settings import GMAPS_API_KEY
from doctor.models import Education, Experience, DoctorStats


def get_origins(origins):
    parameter = 'origins='
    for coordinates in origins:
        parameter += f'{coordinates[0]}, {coordinates[1]}|'
    return parameter


def get_distance_between(origins, destination):
    response = requests.get(
        url='https://maps.googleapis.com/maps/api/distancematrix/json',
        params={
            'origins': get_origins(origins=origins),
            'destinations': f'{destination[0]}, {destination[1]}',
            'key': GMAPS_API_KEY,
        },
    )
    res_json = response.json()
    distances = []
    for item in res_json['rows']:
        elements = item.get('elements')[0]
        if elements['status'] == 'OK':
            distances.append(
                (
                    elements.get('distance', {}).get('text'),
                    elements.get('duration', {}).get('text'),
                ),
            )
        else:
            distances.append(
                (
                    'NA',
                    'NA',
                ),
            )

    return distances


def sort_key(d):
    return d['duration']


def sort_doctors_by_distance(doctors, source):
    doctors_list = []
    doctor_coordinates = [(doctor.get('lat'), doctor.get('long')) for doctor in doctors]
    distances = get_distance_between(doctor_coordinates, source)

    for index, doctor in enumerate(doctors):
        no_of_calls = DoctorStats.objects.filter(doctor_id=doctor['id']).values('no_of_phone_calls')

        doctor['distance'] = distances[index][0]
        doctor['duration'] = distances[index][1]
        doctor['education'] = list(Education.objects.filter(doctor_id=doctor['id']).values())
        doctor['experience'] = list(Experience.objects.filter(doctor_id=doctor['id']).values())
        doctor['no_of_calls'] = no_of_calls[0].get('no_of_phone_calls') if len(no_of_calls) > 0 else 0
        doctors_list.append(doctor)

    return sorted(doctors_list, key=sort_key)




