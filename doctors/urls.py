from django.urls import path
from .views import DoctorCreateView, DoctorListView, DoctorDetailView, AppointmentCreateView, get_doctor_availability

urlpatterns = [
    path('doctors/', DoctorListView.as_view(), name='list-doctors'),
    path('doctors/create/', DoctorCreateView.as_view(), name='create-doctor'),
    path('doctors/<int:pk>/', DoctorDetailView.as_view(), name='doctor-detail'),
    path('appointments/create/', AppointmentCreateView.as_view(), name='create-appointment'),
    path('doctors/<int:doctor_id>/availability/', get_doctor_availability, name='doctor-availability'),
]


