from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import formats
from django.core.urlresolvers import reverse
from person.models import Person


class PersonTest(TestCase):
    def test_main_page_view(self):
        response = self.client.get(reverse('main'))
        context_person = response.context['person']

        self.assertEqual(context_person.pk, 1)

        person = Person.objects.get(pk=1)

        self.assertContains(response, person.name)
        self.assertContains(response, person.surname)
        self.assertContains(response, formats.date_format(person.bithdate, "DATE_FORMAT"))

    def test_save_main_page_data(self):
        self.client.login(username='admin', password='admin')
        response = self.client.post(reverse('edit_home'), {'name': 'Bill', 'bithdate': '1991-01-09'})

        self.assertEqual(Person.objects.all().count(), 1)
        new_item = Person.objects.all()[0]
        self.assertEqual(new_item.name, 'Bill')