from django.urls import path
from api import views


urlpatterns = [
    path('student-api/',views.students_api,name='student-api'),
    path("student-list/",views.student_list,name="student-list")
]
