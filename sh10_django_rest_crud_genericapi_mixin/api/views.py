from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from api.models import Student
from api.serializers import StudentSerializer
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin


# Create your views here.
# class StudentList(GenericAPIView,ListModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     def get(self,request):
#         return self.list(request)
    
# class StudentCreate(GenericAPIView,CreateModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     def post(self,request):
#         return self.create(request)
    
# class StudentRetrive(GenericAPIView,RetrieveModelMixin):

#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     def get(self,request,pk):
#         return self.retrieve(request)
    
# class StudentUpdate(GenericAPIView,UpdateModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     def put(self,request):
#         return self.update(request)
 
# class StudentDelete(GenericAPIView,DestroyModelMixin):
    # queryset = Student.objects.all()
    # serializer_class = StudentSerializer 

    # def delete(self, request, *args, **kwargs):
    #     return self.destroy(request, *args, **kwargs)   
    

class StudentCreateList(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self,request):
        return self.list(request)
    
    def post(self,request):
        return self.create(request)

class StudentRUD(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self,request,*args, **kwargs):
        return self.retrieve(request,*args, **kwargs)
    
    def post(self,request,*args, **kwargs):
        return self.update(request,*args, **kwargs)
    
    def delete(self,request,*args, **kwargs):
        return self.destroy(request,*args, **kwargs)