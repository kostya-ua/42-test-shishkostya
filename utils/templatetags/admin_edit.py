from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django import template
register = template.Library()


@register.inclusion_tag('admin_edit_link.html')
def edit_link(obj):
    content_type = ContentType.objects.get_for_model(obj.__class__)
    link = reverse('admin:%s_%s_change' % (content_type.app_label,
                                           content_type.model), args=(obj.pk,))
    return {'link': link}
