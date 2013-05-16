# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'Knight', fields ['name']
        db.create_unique(u'southtut_knight', ['name'])


        # Changing field 'Knight.apples'
        db.alter_column(u'southtut_knight', 'apples', self.gf('django.db.models.fields.SmallIntegerField')())

    def backwards(self, orm):
        # Removing unique constraint on 'Knight', fields ['name']
        db.delete_unique(u'southtut_knight', ['name'])


        # Changing field 'Knight.apples'
        db.alter_column(u'southtut_knight', 'apples', self.gf('django.db.models.fields.IntegerField')())

    models = {
        u'southtut.knight': {
            'Meta': {'object_name': 'Knight'},
            'apples': ('django.db.models.fields.SmallIntegerField', [], {}),
            'dances_whenever_able': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'of_the_round_table': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['southtut']