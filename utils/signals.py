from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from utils.models import ModelsLog, ACTION_CREATE, ACTION_UPDATE, ACTION_DELETE


IGNORE_LIST = ['ModelsLog']


@receiver(post_save)
def post_save_log(sender, **kwargs):
    model_name = sender._meta.object_name

    if model_name not in IGNORE_LIST:
        action = ACTION_CREATE if kwargs.get('created') else ACTION_UPDATE
        ModelsLog.objects.create(model=model_name, action=action, instance=unicode(kwargs.get('instance')))


@receiver(post_delete)
def post_delete_log(sender, **kwargs):
    model_name = sender._meta.object_name

    if model_name not in IGNORE_LIST:
        ModelsLog.objects.create(model=model_name, action=ACTION_DELETE, instance=unicode(kwargs.get('instance')))