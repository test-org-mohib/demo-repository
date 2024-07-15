from django.test import TestCase
from app.models import Country


# Create your tests here.
class TestCountry(TestCase):
    def setUp(self):
        self.active_student = Country.objects.create(name="Afghanistan")

    def test_afghanistan(self):
        afg = Country.objects.get(name="Afghanistan")
        self.assertEqual(afg.name, "Afghanistan")
