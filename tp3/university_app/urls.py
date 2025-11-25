from django.urls import path
from . import views

urlpatterns = [
    # Student endpoints only
    path('student/add', views.add_student, name='add_student'),
    path('student/getAll', views.get_all_students, name='get_all_students'),
    path('student/getAllUniv', views.get_all_students_university, name='get_all_students_university'),
    path('student/findStudUniv', views.find_students_by_university, name='find_students_by_university'),
]
