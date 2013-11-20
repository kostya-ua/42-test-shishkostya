from django.views.generic import TemplateView
from person.models import Person

class MainPageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(MainPageView, self).get_context_data(**kwargs)
        context["person"] = Person.objects.get(pk=1)
        return context