# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Product.got_price'
        db.add_column('pricecompare_product', 'got_price', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Product.got_price'
        db.delete_column('pricecompare_product', 'got_price')


    models = {
        'pricecompare.product': {
            'Meta': {'object_name': 'Product'},
            'got_price': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
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
