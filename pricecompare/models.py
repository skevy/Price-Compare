from django.db import models

class Source(models.Model):
    name = models.CharField(max_length=255)
    css_selector = models.CharField(max_length=1000)
    regex = models.CharField(max_length=1000)
    
    def __unicode__(self):
        return u'%s' % (self.name)
    
class ProductGroup(models.Model):
    name = models.CharField(max_length=255)
    
    def __unicode__(self):
        return u'%s' % (self.name)
    
class Product(models.Model):
    source = models.ForeignKey(Source)
    product_group = models.ForeignKey(ProductGroup)
    url = models.CharField(max_length=1500)
    price = models.DecimalField(max_digits=10, decimal_places=2, editable=False, null=True, blank=True)
    got_price = models.BooleanField(default=False, editable=False)
    
    def __unicode__(self):
        return u'%s - %s - %s' % (self.source.name, self.product_group.name, self.url)
    
    
    