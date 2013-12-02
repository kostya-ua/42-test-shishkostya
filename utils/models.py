from django.db import models
from django.contrib import admin


ACTION_UNKNOWN = 0
ACTION_CREATE = 1
ACTION_UPDATE = 2
ACTION_DELETE = 3

ACTIONS = (
    (ACTION_UNKNOWN, 'Unknown'),
    (ACTION_CREATE, 'Create'),
    (ACTION_UPDATE, 'Update'),
    (ACTION_DELETE, 'Delete'),
)


class Path(models.Model):
    priority = models.SmallIntegerField(default=0)
    url = models.CharField(max_length=100, unique=True)

    def __unicode__(self):
        return u'%s %d' % (self.url, self.priority)


class Request(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    path = models.ForeignKey(Path)
    method = models.CharField(max_length=8)

    class Meta:
        ordering = ('-date',)

    def __unicode__(self):
        return u'%s %s %s' % (self.date, self.path, self.method)


class ModelsLog(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    model = models.CharField(max_length=40)
    instance = models.CharField(max_length=255)
    action = models.SmallIntegerField(default=0, choices=ACTIONS)


class PathAdmin(admin.ModelAdmin):
    list_display = ('priority', 'url')
    list_filter = ('priority',)
    ordering = ('-priority',)


admin.site.register(Path, PathAdmin)