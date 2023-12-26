from django.urls import path
from api import views

urlpatterns = [
    # path("student-list/",views.StudentList.as_view(),name='student_list'),
    # path("student-retrive/<int:pk>/",views.StudentRetrive.as_view(),name='student_retrive'),
    # path("student-create/",views.StudentCreate.as_view(),name='student_create'),
    # path("student-update/<int:pk>/",views.StudentUpdate.as_view(),name='student_update'),
    # path("student-delete/<int:pk>/",views.StudentDelete.as_view(),name='student_delete'),

    path("student-list/",views.StudentCreateList.as_view(),name='student_list'),
    path("student-rud/<int:pk>/",views.StudentRUD.as_view(),name='student_retrive'),

]
