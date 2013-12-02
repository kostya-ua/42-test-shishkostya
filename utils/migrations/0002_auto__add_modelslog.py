# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ModelsLog'
        db.create_table('utils_modelslog', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('model', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('instance', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('action', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
        ))
        db.send_create_signal('utils', ['ModelsLog'])


    def backwards(self, orm):
        # Deleting model 'ModelsLog'
        db.delete_table('utils_modelslog')


    models = {
        'utils.modelslog': {
            'Meta': {'object_name': 'ModelsLog'},
            'action': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instance': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'utils.request': {
            'Meta': {'object_name': 'Request'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'method': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['utils']