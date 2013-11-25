from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, UpdateView
from person.models import Person
from person.forms import PersonForm


class MainPageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(MainPageView, self).get_context_data(**kwargs)
        context["person"] = Person.objects.get(pk=1)
        return context


class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)


class EditMainPageView(LoginRequiredMixin, UpdateView):
    template_name = "edit.html"
    form_class = PersonForm
    success_url = '/'

    def get_object(self, queryset=None):
        return Person.objects.get(pk=1)

