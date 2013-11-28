import json
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

        response = self.client.post(reverse('edit_home'), {'name': 'Bill', 'bithdate': '1991-01-09',
                                                           'email': 'bill@mail.com'},
                                                            HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        self.assertEqual(Person.objects.all().count(), 1)
        person = Person.objects.all()[0]
        self.assertEqual(person.name, 'Bill')


class CalendarWidgetTest(TestCase):
    def test_widget_showing(self):
        self.client.login(username='admin', password='admin')
        response = self.client.get(reverse('edit_home'))

        self.assertContains(response, '<input id="id_bithdate" type="text" class="datepicker"')
        self.assertContains(response, 'http://code.jquery.com/jquery-1.9.1.js')
        self.assertContains(response, 'http://code.jquery.com/ui/1.10.3/jquery-ui.js')
        self.assertContains(response, 'js/calendar.js')
        self.assertContains(response, 'http://code.jquery.com/ui/1.10.3/themes/smoothness/jquery-ui.css')