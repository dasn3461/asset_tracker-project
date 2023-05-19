from django.shortcuts import render
from rest_framework import viewsets
from .models import Company, Employee, Device, DeviceAssignment
from .serializers import CompanySerializer, EmployeeSerializer, DeviceSerializer, DeviceAssignmentSerializer
# Create your views here.


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class DeviceAssignmentViewSet(viewsets.ModelViewSet):
    queryset = DeviceAssignment.objects.all()
    serializer_class = DeviceAssignmentSerializer
