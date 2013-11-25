from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import formats
from person.models import Person


class PersonTest(TestCase):

    def setUp(self):
        self.person = Person.objects.create(name='John',
                                            surname='Smith',
                                            bithdate='1991-01-09')
        self.user = User.objects.create_user('john', 'john@mail.com', 'password')

    def test_main_page_view(self):
        response = self.client.get('/')
        person = response.context['person']

        self.assertEqual(person.pk, 1)
        self.assertIn(self.person.name, response.content)
        self.assertIn(self.person.surname, response.content)
        self.assertIn(formats.date_format(person.bithdate, "DATE_FORMAT"), response.content)

    def test_save_main_page_data(self):
        self.client.login(username='john', password='password')

        response = self.client.post('/edit_home/', {'name': 'Bill', 'bithdate': '1991-01-09'})

        print response.content

        self.assertEqual(Person.objects.all().count(), 1)
        new_item = Person.objects.all()[0]
        self.assertEqual(new_item.name, 'Bill')
