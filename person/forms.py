from django.forms import ModelForm
from person.models import Person
from widgets import CalendarWidget


class PersonForm(ModelForm):
    class Meta:
        model = Person
        widgets = {
            'bithdate': CalendarWidget(),
        }
