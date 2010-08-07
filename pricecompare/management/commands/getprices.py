from lxml import etree
import urllib2
import re

from django.core.management.base import BaseCommand, CommandError

from pricecompare.models import *

class Command(BaseCommand):

    def handle(self, *args, **options):
        groups = ProductGroup.objects.all()
        for g in groups:
            products = Product.objects.filter(product_group=g)
            for p in products:
                price = self.get_price(p.url, p.source.css_selector, p.source.regex)
                if price:
                    p.price = price
                    p.got_price = True
                    print "%s - success" % p
                else:
                    p.price = "0.00"
                    p.got_price = False
                    print "%s - fail" % p
                p.save()
        
    def get_price(self, url, selector, regex):
        try:
            regex = re.compile(regex)
            html = urllib2.urlopen(url)
            parser = etree.HTMLParser(remove_comments=True)
            tree = etree.parse(html, parser)

            from lxml.cssselect import CSSSelector

            sel = CSSSelector(selector)
        
            price = sel(tree)[0].text.strip('\n\t\r ')
            price = regex.match(price).group('price').replace(",", "")
            return price
        except:
            return None
