from utils.models import Request, Path


class RequestMiddleware(object):

    def process_request(self, request):
        path = Path.objects.get_or_create(url=request.path)[0]
        Request.objects.create(path=path, method=request.method)