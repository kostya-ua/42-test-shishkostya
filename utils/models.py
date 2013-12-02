from django.db import models


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


class Request(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    path = models.CharField(max_length=100)
    method = models.CharField(max_length=8)

    def __unicode__(self):
        return u'%s %s %s' % (self.date, self.path, self.method)


class ModelsLog(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    model = models.CharField(max_length=40)
    instance = models.CharField(max_length=255)
    action = models.SmallIntegerField(default=0, choices=ACTIONS)

