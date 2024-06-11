from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Employee
from .serializers import EmployeeSerializers


@api_view(['POST','GET'])
def welcome(request):
    data= request.data
    print(data)
    return Response('hi this is nandhakumar how are you ?')


@api_view(['GET'])
def getemployee(request):
    employee = Employee.objects.all()
    print(employee)
    serializer = EmployeeSerializers(employee, many=True)
    return Response(serializer.data)

  