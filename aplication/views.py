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

  
@api_view(['POST'])
def addEmployee(request):
   newEmployee = request.data
   serializer= EmployeeSerializers(data=newEmployee, many=True)
   if serializer.is_valid():
       serializer.save()
       return Response(f"new employee successfully added{serializer.data}")
   return Response(serializer.errors)

@api_view(['PUT'])  
def putemployee(request):
    empdata= request.data
    oldemp=Employee.objects.get(id=empdata['id'])
    serializer=EmployeeSerializers(oldemp,data=empdata)
    if serializer.is_valid():
        serializer.save()
        return Response(f'Employee successfully replaced{serializer.data}')
    return Response(serializer.errors)

@api_view(['PATCH'])
def patchemployee(request):
    empdata= request.data
    oldemp=Employee.objects.get(id=empdata['id'])
    serializer=EmployeeSerializers(oldemp,data=empdata,partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(f'Employee successfully modified{serializer.data}')
    return Response(serializer.errors)


@api_view(['DELETE'])
def delemployee(request):
    empdata=request.data
    old=Employee.objects.get(id=empdata['id']).delete()
    return Response("Employee successfully Deleted")

    


