from django.urls import path
from api import views

urlpatterns = [
    path('student-api/',views.StudentAPI.as_view(),name='student_api')

]
