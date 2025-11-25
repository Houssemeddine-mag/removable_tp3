from django.test import TestCase
from django.urls import reverse
from .models import Student, Course, Enrollment
from datetime import date

class StudentModelTest(TestCase):
    def setUp(self):
        self.student = Student.objects.create(
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            date_of_birth=date(2000, 1, 1)
        )

    def test_student_creation(self):
        """Test that a student can be created"""
        self.assertEqual(self.student.first_name, "John")
        self.assertEqual(self.student.last_name, "Doe")
        self.assertEqual(self.student.email, "john.doe@example.com")
        self.assertIsNotNone(self.student.id)


class CourseModelTest(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            name="Introduction to Programming",
            code="CS101",
            credits=3
        )

    def test_course_creation(self):
        """Test that a course can be created"""
        self.assertEqual(self.course.name, "Introduction to Programming")
        self.assertEqual(self.course.code, "CS101")
        self.assertEqual(self.course.credits, 3)
        self.assertIsNotNone(self.course.id)


class EnrollmentModelTest(TestCase):
    def setUp(self):
        self.student = Student.objects.create(
            first_name="Jane",
            last_name="Smith",
            email="jane.smith@example.com",
            date_of_birth=date(1999, 5, 15)
        )
        self.course = Course.objects.create(
            name="Data Structures",
            code="CS201",
            credits=4
        )
        self.enrollment = Enrollment.objects.create(
            student=self.student,
            course=self.course,
            grade="A"
        )

    def test_enrollment_creation(self):
        """Test that an enrollment can be created"""
        self.assertEqual(self.enrollment.student, self.student)
        self.assertEqual(self.enrollment.course, self.course)
        self.assertEqual(self.enrollment.grade, "A")
        self.assertIsNotNone(self.enrollment.id)