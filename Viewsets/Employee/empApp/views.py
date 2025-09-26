from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework import viewsets
# Create your views here.
class EmployeeViewset(viewsets.ViewSet):
    def list(self,request):
        queryset = Employee.objects.all()
        serializer = EmployeeSerializer(queryset,many = True)
        return Response(serializer.data)
    
    def create(self,request):
        serializer = EmployeeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

    def retrieve(self,request,pk = None):
        employee = get_object_or_404(Employee,pk=pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def update(self,request,pk = None):
        employee = get_object_or_404(Employee,pk=pk)
        serializer = EmployeeSerializer(employee,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors)
    
    def delete(self,request,pk=None):
        employee = get_object_or_404(Employee,pk=pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)