from django.test import TestCase
from .models import Student

class StudentModelTest(TestCase):
    def setUp(self):
        # Update these fields to match your actual Student model
        self.student = Student.objects.create(
            name="John Doe",
            # Add other fields that exist in your Student model
        )

    def test_student_creation(self):
        """Test that a student can be created"""
        self.assertIsNotNone(self.student.id)
        self.assertEqual(Student.objects.count(), 1)

    def test_student_str(self):
        """Test the string representation"""
        self.assertIsNotNone(str(self.student))