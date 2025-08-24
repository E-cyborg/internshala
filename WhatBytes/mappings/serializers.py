from rest_framework import serializers
from .models import PatientDoctorMapping
from doctors.serializers import DoctorSerializer

class PatientDoctorMappingSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer(read_only=True)
    doctor_id = serializers.PrimaryKeyRelatedField(
        queryset=PatientDoctorMapping._meta.get_field("doctor").related_model.objects.all(),
        source="doctor",
        write_only=True
    )

    class Meta:
        model = PatientDoctorMapping
        fields ="__all__"
