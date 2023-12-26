from django.urls import path
from api import views

urlpatterns = [
    path('student-api/',views.student_api,name='student_api')
]
