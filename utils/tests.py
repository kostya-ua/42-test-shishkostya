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

    def check_log(self, count, action, model, instance):
        self.assertEqual(ModelsLog.objects.all().count(), count)

        log_entry = ModelsLog.objects.latest('id')
        self.assertEqual(log_entry.action, action)
        self.assertEqual(log_entry.model, model)
        self.assertEqual(log_entry.instance, unicode(instance))

    def test_models_log(self):
        count_before = ModelsLog.objects.all().count()
        model = Request._meta.object_name
        request = Request.objects.create(path='test')

        self.check_log(count_before + 1, ACTION_CREATE, model, request)

        request.path = 'test2'
        request.save()
        self.check_log(count_before + 2, ACTION_UPDATE, model, request)

        request.delete()
        self.check_log(count_before + 3, ACTION_DELETE, model, request)