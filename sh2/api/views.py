from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from api.serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt 
from api.models import Student
from api.serializer import StudentSerializer

# Create your views here.

@csrf_exempt
def students_api(request):
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythondata)
        print(serializer)

        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Insert Successfuly'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')

        return HttpResponse(JSONRenderer().render(serializer.errors),content_type='application/json')

def student_list(request):
    student_list = Student.objects.all()
    serializer = StudentSerializer(student_list,many=True)

    student_json = JSONRenderer().render(serializer.data)
    return HttpResponse(student_json,content_type="application/json")

    # return JsonResponse(serializer.data,safe=False)
