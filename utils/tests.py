from django.test import TestCase
from django.conf import settings
from utils.models import Request
from utils.views import RequestsView


class UtilsTest(TestCase):

    def setUp(self):
        for i in range(11):
            Request.objects.create(path='/test%d' % 1)

    def test_requests_view(self):
        view = RequestsView()
        context = view.get_context_data()

        self.assertEqual(len(context['requests_list']), 10)

    def test_context_processor(self):
        response = self.client.get('/')
        self.assertIn('SETTINGS', response.context)
        self.assertEqual(response.context['SETTINGS'], settings)