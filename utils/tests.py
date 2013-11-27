from django.test import TestCase
from django.conf import settings
from django.core.urlresolvers import reverse
from utils.models import Request
from utils.views import RequestsView


class UtilsTest(TestCase):
    def test_requests_view(self):
        response = self.client.get(reverse('request_list'))
        self.assertContains(response, reverse('request_list'))

    def test_view_only_ten(self):
        for i in range(11):
            Request.objects.create(path='/test%d' % 1)

        view = RequestsView()
        context = view.get_context_data()

        self.assertEqual(len(context['requests_list']), 10)

    def test_context_processor(self):
        response = self.client.get('/requests/')
        self.assertIn('SETTINGS', response.context)
        self.assertEqual(response.context['SETTINGS'], settings)