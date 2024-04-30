from django.test import TestCase

from .models import Point

class PointModelTests(TestCase):
    def test_lat_is_less_than_90(self):
        point = Point(location='Location1', latitude=80.0)
        self.assertIs(point.latitude > 90, False)
