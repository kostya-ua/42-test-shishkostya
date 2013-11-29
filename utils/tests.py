from django.test import TestCase
from django.conf import settings
from django.core.urlresolvers import reverse
from django.template import Template, Context
from django.contrib.auth.models import User
from utils.models import Request, ModelsLog, ACTION_CREATE,  ACTION_UPDATE, ACTION_DELETE
from utils.views import RequestsView


def render_template(template, **kwargs):
    return Template(template).render(Context(**kwargs))


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
        response = self.client.get(reverse('request_list'))
        self.assertIn('SETTINGS', response.context)
        self.assertEqual(response.context['SETTINGS'], settings)

    def test_edit_link_tag(self):
        user = User.objects.get(pk=1)
        rendered = render_template(
            '{% load admin_edit %}'
            '{% edit_link user %}', dict_={'user': user})

        change_link = reverse('admin:auth_user_change', args=(user.pk,))

        self.assertEqual(rendered, '<a href="%s">(admin)</a>' % change_link)

    def test_models_log_object(self):
        request = Request.objects.create(path='test')

        self.assertEqual(ModelsLog.objects.all().count(), 1)

        log_entry = ModelsLog.objects.get(pk=1)
        self.assertEqual(log_entry.action, ACTION_CREATE)
        self.assertEqual(log_entry.model, Request._meta.object_name)

        request.path = 'test2'
        request.save()

        self.assertEqual(ModelsLog.objects.all().count(), 2)

        log_entry = ModelsLog.objects.get(pk=2)
        self.assertEqual(log_entry.action, ACTION_UPDATE)
        self.assertEqual(log_entry.model, Request._meta.object_name)

        request.delete()

        self.assertEqual(ModelsLog.objects.all().count(), 3)

        log_entry = ModelsLog.objects.get(pk=3)
        self.assertEqual(log_entry.action, ACTION_DELETE)
        self.assertEqual(log_entry.model, Request._meta.object_name)