from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework import viewsets
from .pagination import CustomPagination
from .filters import EmployeeFilter

# from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.
class EmployeeViewset(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = CustomPagination
    # filterset_fields = ['designation']  
    # custom filter
    # filter_backends = [DjangoFilterBackend]

    filterset_class = EmployeeFilter
