from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer


@api_view(['POST'])
def add_student(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response("New student is added", status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_all_students(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_all_students_university(request):
    students = Student.objects.select_related('university').all()
    result = [
        {
            'student_name': student.name,
            'university_name': student.university.name
        }
        for student in students
    ]
    return Response(result)


@api_view(['GET'])
def find_students_by_university(request):
    univ_name = request.GET.get('univName')
    if not univ_name:
        return Response({"error": "univName parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
    
    students = Student.objects.select_related('university').filter(university__name=univ_name)
    result = [
        {
            'student_name': student.name,
            'university_name': student.university.name
        }
        for student in students
    ]
    return Response(result)
