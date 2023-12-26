from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Student
from api.serializers import StudentSerializer

# Create your views here.
@api_view(['GET','POST','PUT','PATCH','DELETE'])
def student_api(request,id=None):
    if request.method=="GET":
        # id = request.data.get('id')
        id=id
        if id is not None:
            student = Student.objects.get(id=id)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        
        all_student = Student.objects.all()
        serializer = StudentSerializer(all_student,many=True)
        return Response(serializer.data)

    if request.method=="POST":
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Data insert successfully"})
        
        return Response(serializer.errors)
    
    if request.method=='PUT':
        # id = request.data.get('id')
        id=id

        student = Student.objects.get(id=id)

        serializer = StudentSerializer(student,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Data complete  update successfully"})
        
        return Response(serializer.errors)
    
    if request.method=='PATCH':
        # id = request.data.get('id')
        id=id

        student = Student.objects.get(id=id)

        serializer = StudentSerializer(student,data=request.data,partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Data update successfully"})
        
        return Response(serializer.errors)
    
    if request.method == "DELETE":
        id = id
        student = Student.objects.get(id=id)
        student.delete()
        return Response({"msg":"Data Delete successfully"})
    
