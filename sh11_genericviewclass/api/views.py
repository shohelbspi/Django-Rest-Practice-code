from django.shortcuts import render
from api.models import Student
from api.serializer import StudentSerializer
# from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

# Create your views here.

# class get_student(ListAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# class create_student(CreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# class retrieve_student(RetrieveAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# class update_student(UpdateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# class delete_student(DestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer   

class StudentListCreateView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
