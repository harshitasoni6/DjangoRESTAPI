from django.shortcuts import render
from django.http import JsonResponse
from app.models import Student
from app.serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.
# Function Based View
# static way using Web Application Endpoints
# def studentView(request):
    # students ={
    #     'id' : 1,
    #     'name' : 'Rathan',
    #     'class' : 'CSE'
    # }
    # return HttpResponse(students)
# API endpoint
# def studentView(request):
    # students ={
    #     'id' : 1,
    #     'name' : 'Rathan',
    #     'class' : 'CSE'
    # }
    # return JsonResponse(students)
# manully serialization
# def studentView(request):
#     students = Student.objects.all()
#     students_list = list(students.values())
#     return JsonResponse(students_list,safe = False)
# dynamic way
@api_view(['GET','POST'])
def studentView(request):
    if request.method == 'GET':
        #get all the data from the student table
        students = Student.objects.all()
        serializer = StudentSerializer(students,many = True)
        return Response(serializer.data,status = status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','PUT','DELETE']) 
def studentDetailView(request,pk):
    try:
        student = Student.objects.get(pk=pk)
    except:
        return Response(status = status.HTTP_404_NOT_FOUND)
    if request.method =='GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data,status = status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = StudentSerializer(student,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
