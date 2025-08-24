from django.urls import path
from .views import PatientListCreateView, PatientDetailView

urlpatterns = [
    path("", PatientListCreateView.as_view(), name="patients-list-create"),
    path("<int:pk>/", PatientDetailView.as_view(), name="patients-detail"),
]
