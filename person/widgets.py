from django.forms.widgets import DateInput
from django.conf import settings


class CalendarWidget(DateInput):
    def __init__(self, attrs={}):
        attrs.update({'class': 'datepicker'})
        super(CalendarWidget, self).__init__(attrs=attrs)

    class Media:
        js = ('http://code.jquery.com/jquery-1.9.1.js',
              'http://code.jquery.com/ui/1.10.3/jquery-ui.js',
              settings.STATIC_URL + 'js/calendar.js')

        css = {'all': ('http://code.jquery.com/ui/1.10.3/themes/smoothness/jquery-ui.css', )}
