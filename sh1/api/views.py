from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from api.models import Student
from api.serializers import StudentSerializers
from rest_framework.renderers import JSONRenderer

# Create your views here.

def get_single_student(request):
    students = Student.objects.get(id=1)
    serializer = StudentSerializers(students)

    # student_json = JSONRenderer().render(serializer.data)
    # return HttpResponse(student_json,content_type='application/json')

    return JsonResponse(serializer.data)

def student_list(request):
    student_list = Student.objects.all()
    serializer = StudentSerializers(student_list,many=True)

    # student_json = JSONRenderer().render(serializer.data)
    # return HttpResponse(student_json,content_type="application/json")

    return JsonResponse(serializer.data,safe=False)

