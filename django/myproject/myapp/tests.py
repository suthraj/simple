##### .../myapp/tests.py #####

from django.test import TestCase
from myapp.models import Person, Shirt, Student

# Create your tests here.

"""
    Test the model: 'Person'.
"""
class PersonTestCase(TestCase):
    def setUp(self):
        Person.objects.create(first_name="Hulk", last_name="Hogan")
        Person.objects.create(first_name="Peter", last_name="Pan")

    """
        Test scenarios where the testcases are expected to SUCCEED.
    """
    # Simple test case to retrieve and verify first names from DB.
    def test_person_basic_01(self):
        f_name_aa = Person.objects.get(first_name="Hulk")
        f_name_bb = Person.objects.get(first_name="Peter")
        self.assertEqual(f_name_aa.first_name, 'Hulk')
        self.assertEqual(f_name_bb.first_name, 'Peter')


"""
    Test the model: 'Shirt'.
"""
class ShirtTestCase(TestCase):
    def setUp(self):
        Shirt.objects.create(name="Hulk", shirt_size="s")
        Shirt.objects.create(name="Peter", shirt_size="m")

    """
        Test scenarios where the testcases are expected to SUCCEED.
    """
    # Simple test case to retrieve and verify first names from DB.
    def test_shirt_basic_01(self):
        shirt_aa = Shirt.objects.get(name="Hulk")
        shirt_bb = Shirt.objects.get(name="Peter")
        self.assertEqual(shirt_aa.shirt_size, 's')
        self.assertEqual(shirt_bb.shirt_size, 'm')


"""
    Test the model: 'Student'.
"""
class StudentTestCase(TestCase):
    def setUp(self):
        Student.objects.create(id=11111, first_name="Anna", last_name="Peterson", age=21)
        Student.objects.create(id=12345, first_name="Gina", last_name="Jordan", age=45)

    """
        Test scenarios where the testcases are expected to SUCCEED.
    """
    # Simple test case to retrieve and verify data from DB.
    def test_person_basic_01(self):
        a = Student.objects.get(first_name="Anna")
        b = Student.objects.get(first_name="Gina")
        self.assertEqual(a.age, 21)
        self.assertEqual(b.age, 45)

    """
        Test scenarios where the testcases are expected to FAIL.
        - The following testcases return 'True' if testcase raises an error.
    """
    # Case-sensitivity test.
    def test_person_case_sensitive_01(self):
        with self.assertRaises(Exception):
            a = Student.objects.get(first_name="anna")
            #self.fail("TEST-PASSED: Case sensitivity confirmed")
