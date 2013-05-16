# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Knight.apples'
        db.delete_column(u'southtut_knight', 'apples')

        # Adding field 'Knight.apple'
        db.add_column(u'southtut_knight', 'apple',
                      self.gf('django.db.models.fields.SmallIntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Knight.apples'
        db.add_column(u'southtut_knight', 'apples',
                      self.gf('django.db.models.fields.SmallIntegerField')(default=0),
                      keep_default=False)

        # Deleting field 'Knight.apple'
        db.delete_column(u'southtut_knight', 'apple')


    models = {
        u'southtut.knight': {
            'Meta': {'object_name': 'Knight'},
            'apple': ('django.db.models.fields.SmallIntegerField', [], {}),
            'dances_whenever_able': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'of_the_round_table': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['southtut']