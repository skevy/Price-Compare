# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Source'
        db.create_table('pricecompare_source', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('css_selector', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('regex', self.gf('django.db.models.fields.CharField')(max_length=1000)),
        ))
        db.send_create_signal('pricecompare', ['Source'])

        # Adding model 'ProductGroup'
        db.create_table('pricecompare_productgroup', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('pricecompare', ['ProductGroup'])

        # Adding model 'Product'
        db.create_table('pricecompare_product', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('source', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pricecompare.Source'])),
            ('product_group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pricecompare.ProductGroup'])),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=1500)),
        ))
        db.send_create_signal('pricecompare', ['Product'])


    def backwards(self, orm):
        
        # Deleting model 'Source'
        db.delete_table('pricecompare_source')

        # Deleting model 'ProductGroup'
        db.delete_table('pricecompare_productgroup')

        # Deleting model 'Product'
        db.delete_table('pricecompare_product')


    models = {
        'pricecompare.product': {
            'Meta': {'object_name': 'Product'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product_group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pricecompare.ProductGroup']"}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pricecompare.Source']"}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '1500'})
        },
        'pricecompare.productgroup': {
            'Meta': {'object_name': 'ProductGroup'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'pricecompare.source': {
            'Meta': {'object_name': 'Source'},
            'css_selector': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'regex': ('django.db.models.fields.CharField', [], {'max_length': '1000'})
        }
    }

    complete_apps = ['pricecompare']
