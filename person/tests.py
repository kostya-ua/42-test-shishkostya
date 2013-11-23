from django.test import TestCase
from django.utils import formats
from person.models import Person


class PersonTest(TestCase):

    def setUp(self):
        self.person = Person.objects.create(name='John',
                                            surname='Smith',
                                            bithdate='1991-01-09')

    def test_main_page_view(self):
        response = self.client.get('/')
        person = response.context['person']

        self.assertEqual(person.pk, 1)
        self.assertIn(self.person.name, response.content)
        self.assertIn(self.person.surname, response.content)
        self.assertIn(formats.date_format(person.bithdate, "DATE_FORMAT"), response.content)

