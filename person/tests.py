from django.test import TestCase
from django.utils import formats
from django.core.urlresolvers import reverse
from person.models import Person


class PersonTest(TestCase):

    def setUp(self):
        Person.objects.create(name='John',
                              surname='Smith',
                              bithdate='1991-01-09')

    def test_main_page_view(self):
        response = self.client.get(reverse('main'))
        context_person = response.context['person']

        self.assertEqual(context_person.pk, 1)

        person = Person.objects.get(pk=1)

        self.assertContains(response, person.name)
        self.assertContains(response, person.surname)
        self.assertContains(response, formats.date_format(person.bithdate, "DATE_FORMAT"))
