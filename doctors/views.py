from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Doctor, Appointment
from .serializers import DoctorSerializer, AppointmentSerializer
from django.utils.dateparse import parse_datetime
from django.db.models import Q


# 1. Create Doctor
class DoctorCreateView(generics.CreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


# 2. List Doctors
class DoctorListView(generics.ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


# 3. Get Doctor Details
class DoctorDetailView(generics.RetrieveAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


# 4. Create Appointment for Doctor
class AppointmentCreateView(generics.CreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def perform_create(self, serializer):
        doctor = serializer.validated_data['doctor']
        start_datetime = serializer.validated_data['start_datetime']
        end_datetime = serializer.validated_data['end_datetime']

        # Check if appointment overlaps with existing appointments
        overlapping_appointments = Appointment.objects.filter(
            doctor=doctor,
            start_datetime__lt=end_datetime,
            end_datetime__gt=start_datetime
        ).exists()

        if overlapping_appointments:
            raise serializers.ValidationError("This time slot is already booked.")

        serializer.save()


# 5. Get Doctor Availability
@api_view(['GET'])
def get_doctor_availability(request, doctor_id):
    start_date = request.query_params.get('start')
    end_date = request.query_params.get('end')

    doctor = Doctor.objects.get(id=doctor_id)
    appointments = Appointment.objects.filter(
        doctor=doctor,
        start_datetime__gte=start_date,
        end_datetime__lte=end_date
    )

    availability_slots = []
    # Calculate availability slots in 15-minute intervals here
    # Ensure it accounts for appointments and doctor's availability hours

    return Response(availability_slots)
