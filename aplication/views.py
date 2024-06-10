from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['POST','GET'])
def welcome(request):
    data= request.data
    print(data)
    return Response('hi this is nandhakumar how are you ?')
