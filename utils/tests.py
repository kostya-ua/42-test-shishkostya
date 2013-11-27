from django.test import TestCase
from django.core.urlresolvers import reverse
from utils.models import Request
from utils.views import RequestsView


class RequestsTest(TestCase):
    def test_requests_view(self):
        response = self.client.get(reverse('request_list'))
        self.assertContains(response, reverse('request_list'))

    def test_view_only_ten(self):
        for i in range(11):
            Request.objects.create(path='/test%d' % 1)

        view = RequestsView()
        context = view.get_context_data()

        self.assertEqual(len(context['requests_list']), 10)

