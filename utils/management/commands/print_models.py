from django.contrib.contenttypes.models import ContentType
from django.core.management.base import NoArgsCommand


def count_models():
    result = []

    for content_type in ContentType.objects.all():
        model = content_type.model_class()
        if model:
            result.append((model.__module__, model.__name__, model._default_manager.count()))

    return result


class Command(NoArgsCommand):
    help = 'Command that prints all project models and the count of objects in every model.'

    def handle_noargs(self, **options):
        for module, name, count in count_models():
            print "%s.%s\t%d" % (module, name, count)