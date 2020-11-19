from django.test import TestCase


class ViewTest(TestCase):
    def test_home_page(self):
        response = self.client.get('/')
        print('Response status code : ' + str(response.status_code))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
