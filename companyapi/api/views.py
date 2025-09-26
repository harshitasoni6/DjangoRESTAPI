from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action 
from rest_framework.response import Response
from api.models import Company
from api.models import Employee
from api.serializers import CompanySerializer
from api.serializers import EmployeeSerializer
from .pagination import CustomPagination
# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h2>Welcome to Company API 🚀</h2><p>Go to <a href='/api/v1/companies/'>Companies API</a></p>")

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    # companies/{company_id}/employees/
    @action(detail = True,methods = ['get'])
    def employees(self,request,pk = None):
        try:
            company = Company.objects.get(pk = pk)
            emps = Employee.objects.filter(company = company)
            emps_serializer = EmployeeSerializer(emps,many=True,context = {'request':request})
            return Response(emps_serializer.data)
        except Exception as e:
            print(e)
            return Response({'message':'Company might not exist!! Error!!'})
    

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = CustomPagination