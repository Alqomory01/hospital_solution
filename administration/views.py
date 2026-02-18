from django.shortcuts import render
from django.http import HttpResponse 
from rest_framework import generics 
from rest_framework.permissions import AllowAny 
from rest_framework.response import Response 
from rest_framework.views import APIView 
from rest_framework_simplejwt.views import TokenObtainPairView 
from .models import CustomUser 
from .serializers import UserSerializer
from .permissions import IsRole
from .permissions import RolePermission
def home(request): 
    return HttpResponse("Welcome to the Hospital Management System")

class RegisterView(generics.CreateAPIView): 
    queryset = CustomUser.objects.all() 
    serializer_class = UserSerializer 
    permission_classes = [AllowAny]
class RoleDashboardView(APIView): 
    def get(self, request): 
        role = request.user.role 
        if role == 'Doctor': 
            return Response({"dashboard": "Doctor view: appointments, patients, prescriptions"}) 
        elif role == 'Patient': 
            return Response({"dashboard": "Patient view: results, appointments, billing"}) 
        elif role == 'Pharmacist': return Response({"dashboard": "Pharmacist view: prescriptions, inventory"}) 
        elif role == 'Admin': return Response({"dashboard": "Admin view: user management, reports"}) 
        elif role == 'Nurse': return Response({"dashboard": "Nurse view: patient care tasks"}) 
        elif role == 'LabTech': return Response({"dashboard": "LabTech view: lab tests, results"}) 
        else: return Response({"dashboard": f"{role} view not yet implemented"})

class DoctorView(APIView): 
    permission_classes = [RolePermission]
    allowed_roles = ['Doctor']
    def get(self, request): 
        return Response({"message": "Doctor-only endpoint"})
class PatientView(APIView):
    permission_classes = [IsRole('Patient')]
    def get(self, request):
        return Response({"message": "Patient-only endpoint"})
class PharmcayView(APIView):
    permission_classes = [IsRole('Pharmacist')]
    def get(self, request):
        return Response({"message": "Pharmacy-only endpoint"})
class AdminView(APIView): 
    permission_classes = [RolePermission] 
    allowed_roles = ['Admin'] # Only Admins can access 
    def get(self, request): 
        return Response({ "dashboard": "Admin-only view: manage users, departments, audit logs, reports" })   
# Create your views here.
