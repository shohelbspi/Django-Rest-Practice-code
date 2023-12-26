from django.urls import path
from api import views

urlpatterns = [
    path("",views.get_single_student,name="get-single-student"),
    path("student-list",views.student_list,name="student-list")
]
