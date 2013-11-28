from optparse import make_option
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
    option_list = NoArgsCommand.option_list + (
        make_option('--stderr',
                    action='store_true',
                    dest='stderr_output',
                    default=False,
                    help='Dublicate output to STDERR.'),
                    )

    def handle_noargs(self, **options):
        for module, name, count in count_models():
            message = "%s.%s\t%d\n" % (module, name, count)

            self.stdout.write(message)
            if options['stderr_output']:
                self.stderr.write("error: %s" % message)