from django.views.generic import TemplateView
from utils.models import Request


class RequestsView(TemplateView):
    template_name = 'requests.html'

    def get_context_data(self, **kwargs):
        context = super(RequestsView, self).get_context_data(**kwargs)
        last_ten = Request.objects.all()[:10]
        context["requests_list"] = sorted(last_ten, key=lambda o: -o.path.priority)

        return context