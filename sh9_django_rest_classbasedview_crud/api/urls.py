from django.urls import path
from api import views

urlpatterns = [
    path('student-api/',views.StudentApi.as_view(),name='student_api'),
    path('student-api/<int:pk>/',views.StudentApi.as_view(),name='student_api_id')
]
