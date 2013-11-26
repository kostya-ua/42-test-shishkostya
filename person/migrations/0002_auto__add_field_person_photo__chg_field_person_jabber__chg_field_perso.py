# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Person.photo'
        db.add_column('person_person', 'photo',
                      self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100),
                      keep_default=False)


        # Changing field 'Person.jabber'
        db.alter_column('person_person', 'jabber', self.gf('django.db.models.fields.CharField')(max_length=40))

        # Changing field 'Person.email'
        db.alter_column('person_person', 'email', self.gf('django.db.models.fields.CharField')(max_length=40))

    def backwards(self, orm):
        # Deleting field 'Person.photo'
        db.delete_column('person_person', 'photo')


        # Changing field 'Person.jabber'
        db.alter_column('person_person', 'jabber', self.gf('django.db.models.fields.CharField')(max_length=20))

        # Changing field 'Person.email'
        db.alter_column('person_person', 'email', self.gf('django.db.models.fields.CharField')(max_length=20))

    models = {
        'person.person': {
            'Meta': {'object_name': 'Person'},
            'bio': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'bithdate': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'other_contacts': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'})
        }
    }

    complete_apps = ['person']