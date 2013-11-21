from django.test import TestCase
from person.models import Person


class PersonTest(TestCase):

    def setUp(self):
        Person.objects.create(name='John', bithdate='1989-05-13')


    def test_main_page_view(self):
        response = self.client.get('/')
        person = response.context['person']
        self.assertEqual(person.pk, 1)
