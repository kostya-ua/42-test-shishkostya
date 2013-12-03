# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        db.rename_column('utils_request', 'new_path_id', 'path_id')

    def backwards(self, orm):
        db.rename_column('utils_request', 'path_id', 'new_path_id')


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
            'path': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['utils.Path']"})
        }
    }

    complete_apps = ['utils']