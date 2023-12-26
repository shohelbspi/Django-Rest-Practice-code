from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import Student
from api.serializers import StudentSerializer

# Create your views here.

class StudentApi(APIView):
    
    def get(self,request,format=None,pk=None):
        id = pk
        if id is not None:
            student = Student.objects.get(pk=id)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        
        all_student = Student.objects.all()
        serializer = StudentSerializer(all_student,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":'Data Create Successfully'})
        
        return Response(serializer.errors)
    
    def put(self,request,pk):
        id = pk
        student = Student.objects.get(pk=id)
        serailizer = StudentSerializer(student,data=request.data)
        if serailizer.is_valid():
            serailizer.save()
            return Response({'msg':"Student Complete Update Successfully "})
        
        return Response(serailizer.errors)
    
    def patch(self,request,pk):
        id = pk
        student = Student.objects.get(pk=id)
        serializer = StudentSerializer(student,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"Student parital Update Successfully "})
        
        return Response(serializer.errors)

    def delete(self, request, pk):
        id = pk
        student = Student.objects.get(pk=id)
        student.delete()
        return Response({'msg':'Data delete Successfully'})
