# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models
from utils.helpers import db_table_exists

class Migration(SchemaMigration):

    def forwards(self, orm):
        if db_table_exists(u'person_person'):
            db.delete_table(u'person_person')

        # Adding model 'Person'
        db.create_table(u'person_person', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('surname', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('bithdate', self.gf('django.db.models.fields.DateField')()),
            ('bio', self.gf('django.db.models.fields.TextField')()),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('skype', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('jabber', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('other_contacts', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'person', ['Person'])


    def backwards(self, orm):
        # Deleting model 'Person'
        db.delete_table(u'person_person')


    models = {
        u'person.person': {
            'Meta': {'object_name': 'Person'},
            'bio': ('django.db.models.fields.TextField', [], {}),
            'bithdate': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'other_contacts': ('django.db.models.fields.TextField', [], {}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['person']