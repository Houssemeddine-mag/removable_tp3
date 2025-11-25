from django.test import TestCase
from .models import Student
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

    def test_student_count(self):
        """Test that student count is correct"""
        count = Student.objects.count()
        self.assertEqual(count, 1)