from django.shortcuts import render
from rest_framework.views import APIView
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework import mixins,generics

# Create your views here.

class Employees(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


# class EmployeesDetails(generics.RetrieveAPIView,generics.UpdateAPIView,generics.DestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     lookup_field = 'pk'


# instead of using these three generics.RetrieveAPIView,generics.UpdateAPIView,generics.DestroyAPIView 
# we can use generics.RetrieveUpdateDestroyAPIView
class EmployeesDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'pk'

