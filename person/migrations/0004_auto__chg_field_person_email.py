# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Person.email'
        db.alter_column('person_person', 'email', self.gf('django.db.models.fields.EmailField')(max_length=75))

    def backwards(self, orm):

        # Changing field 'Person.email'
        db.alter_column('person_person', 'email', self.gf('django.db.models.fields.CharField')(max_length=40))

    models = {
        'person.person': {
            'Meta': {'object_name': 'Person'},
            'bio': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'bithdate': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'other_contacts': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'})
        }
    }

    complete_apps = ['person']