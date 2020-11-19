import datetime
from django.test import TestCase
from visitorx.models import Visit


class VisitModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Visit.objects.create(
            http_user_agent='wget',
            remote_addr='127.0.0.1',
            last_visit=datetime.datetime.now(),
        )

    def test_str(self):
        visit = Visit.objects.get(id=1)
        self.assertEqual(str(visit), '<Visit #1>')
