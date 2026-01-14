from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    RegisterView,
    PatientListCreateView,
    PatientRetrieveUpdateDestroyView,
    DoctorListCreateView,
    DoctorRetrieveUpdateDestroyView,
    MappingListCreateView,
    MappingByPatientView,
    MappingDestroyView,
)

urlpatterns = [
    # Auth
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Patients
    path('patients/', PatientListCreateView.as_view(), name='patients_list_create'),
    path('patients/<int:pk>/', PatientRetrieveUpdateDestroyView.as_view(), name='patients_detail'),

    # Doctors
    path('doctors/', DoctorListCreateView.as_view(), name='doctors_list_create'),
    path('doctors/<int:pk>/', DoctorRetrieveUpdateDestroyView.as_view(), name='doctors_detail'),

    # Mappings
    path('mappings/', MappingListCreateView.as_view(), name='mappings_list_create'),
    path('mappings/patient/<int:patient_id>/', MappingByPatientView.as_view(), name='mappings_by_patient'),
    path('mappings/<int:pk>/', MappingDestroyView.as_view(), name='mappings_delete'),

]