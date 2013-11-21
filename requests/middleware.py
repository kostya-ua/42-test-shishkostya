from requests.models import Request


class RequestMiddleware(object):

    def process_request(self, request):
        Request.objects.create(path=request.path, method=request.method)