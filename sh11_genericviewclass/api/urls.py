from django.urls import path
from api import views

urlpatterns = [
    # path('get-student/',views.get_student.as_view(),name='get_student'),
    # path('create-student/',views.create_student.as_view(),name='create_student'),
    # path('retrieve-student/<int:pk>/',views.retrieve_student.as_view(),name='retrieve_student'),
    # path('update-student/<int:pk>/',views.update_student.as_view(),name='update_student'),
    # path('delete-student/<int:pk>/',views.delete_student.as_view(),name='delete_student'),

    path('student-list-create/',views.StudentListCreateView.as_view(),name='student_list_create'),
    path('student-rud/<int:pk>/',views.StudentRetrieveUpdateDeleteView.as_view(),name='student_rud')
]

