import json
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseBadRequest
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

    def get_success_url(self):
        return reverse('main')

    def get_object(self, queryset=None):
        return Person.objects.get(pk=1)

    def form_valid(self, form):
        if self.request.is_ajax():
            self.object = form.save()

            return HttpResponse(json.dumps("Form saved successful."), mimetype="application/json")

        return super(EditMainPageView, self).form_valid(form)

    def form_invalid(self, form):
        print form.errors
        if self.request.is_ajax():
            return HttpResponse(json.dumps({'errors': form.errors}), mimetype="application/json")

        return super(EditMainPageView, self).form_invalid(form)