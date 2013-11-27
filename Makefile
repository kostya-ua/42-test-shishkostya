MANAGE=django-admin.py
PYTHONPATH=$(CURDIR)
SETTINGS=test_assignment.settings

run:
	PYTHONPATH=$(PYTHONPATH) DJANGO_SETTINGS_MODULE=$(SETTINGS) $(MANAGE) runserver

test:
	PYTHONPATH=$(PYTHONPATH) DJANGO_SETTINGS_MODULE=$(SETTINGS) $(MANAGE) test person

syncdb:
	PYTHONPATH=$(PYTHONPATH) DJANGO_SETTINGS_MODULE=$(SETTINGS) $(MANAGE) syncdb --noinput
