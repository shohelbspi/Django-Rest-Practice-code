from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from api.models import Student
from api.serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def student_api(request):
    if request.method == "GET":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id',None)

        if id is not None:
            student = Student.objects.get(id=id)
            serializer = StudentSerializer(student)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')

        all_student = Student.objects.all()
        serializer = StudentSerializer(all_student,many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')
    
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythondata)

        if serializer.is_valid():
            serializer.save()

            res = {'msg':"Data insert successfullt"}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    
    if request.method=="PUT":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')

        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student,data=pythondata,partial=True)

        if serializer.is_valid():
            serializer.save()
            res = {'msg':"Data update successfullt"}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    
    if request.method=="DELETE":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')

        student = Student.objects.get(id=id)
        student.delete()
        res = {'msg':"Data delete successfullt"}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data,content_type='application/json')

