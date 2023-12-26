from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

# @api_view()
# def getStudent(request):
#     return Response({'msg':"Hello World "})

# @api_view(['GET'])
# def getStudent(request):
#     return Response({'msg':"Hello World "})

# @api_view(['POST'])
# def getStudent(request):
#     if request.method == "POST":
#         print(request.data)
#         return Response({'msg':"Hello World "})

@api_view(['GET','POST'])
def getStudent(request):
    if request.method == "GET":
        return Response({'msg':"This is Get Response"})

    if request.method == "POST":
        print(request.data)
        return Response({'msg':"This is Post Response",'data':request.data})
