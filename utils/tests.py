from django.test import TestCase
from requests.models import Request
from requests.views import RequestsView


class RequestsTest(TestCase):

    def setUp(self):
        for i in range(11):
            Request.objects.create(path='/test%d' % 1)

    def test_requests_view(self):
        view = RequestsView()
        context = view.get_context_data()

        self.assertEqual(len(context['requests_list']), 10)