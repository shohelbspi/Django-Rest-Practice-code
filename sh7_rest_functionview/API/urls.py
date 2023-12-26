from django.urls import path
from API import views

urlpatterns = [
    path('student-api/',views.getStudent,name="get_student")
]
