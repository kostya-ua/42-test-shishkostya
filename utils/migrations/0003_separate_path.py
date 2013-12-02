# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        # Note: Don't use "from appname.models import ModelName". 
        # Use orm.ModelName to refer to models in this application,
        # and orm['appname.ModelName'] for models in other applications.
        db.create_table('utils_path', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('priority', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('url', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
        ))

        db.add_column('utils_request', 'new_path',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['utils.path']),
                      keep_default=False)

        for obj in orm['utils.request'].objects.all():
            path = orm['utils.path'].objects.get_or_create(url=obj.path)[0]
            obj.new_path = path
            obj.save()

        db.delete_column('utils_request', 'path')


    def backwards(self, orm):
        "Write your backwards methods here."

        db.add_column('utils_request', 'path',
                      self.gf('django.db.models.fields.CharField')(max_length=100), keep_default=False)

        for obj in orm['utils.request'].objects.all():
            obj.path = obj.new_path.url
            obj.save()

        db.delete_column('utils_request', 'new_path')
        db.delete_table('utils_path')

    models = {
        'utils.modelslog': {
            'Meta': {'object_name': 'ModelsLog'},
            'action': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instance': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'utils.path': {
            'Meta': {'object_name': 'Path'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'priority': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'url': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        'utils.request': {
            'Meta': {'ordering': "('-date',)", 'object_name': 'Request'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'method': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'new_path': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['utils.Path']"}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['utils']
    symmetrical = True
