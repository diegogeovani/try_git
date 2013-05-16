# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Knight.dances_whenever_able'
        db.add_column(u'southtut_knight', 'dances_whenever_able',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Knight.apples'
        db.add_column(u'southtut_knight', 'apples',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Knight.dances_whenever_able'
        db.delete_column(u'southtut_knight', 'dances_whenever_able')

        # Deleting field 'Knight.apples'
        db.delete_column(u'southtut_knight', 'apples')


    models = {
        u'southtut.knight': {
            'Meta': {'object_name': 'Knight'},
            'apples': ('django.db.models.fields.IntegerField', [], {}),
            'dances_whenever_able': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'of_the_round_table': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['southtut']