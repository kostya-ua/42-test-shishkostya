from django.views.generic import TemplateView
from requests.models import Request


class RequestsView(TemplateView):
    template_name = 'requests.html'

    def get_context_data(self, **kwargs):
        context = super(RequestsView, self).get_context_data(**kwargs)
        context["requests_list"] = Request.objects.all().order_by("-date")[:10]
        
        return context