from lxml import etree
import urllib2
import re

#Amazon
#URL = "http://www.amazon.com/Samsung-UN55C8000-55-Inch-1080p-HDTV/dp/B0036WT4KG/ref=sr_1_1?ie=UTF8&s=electronics&qid=1279746995&sr=8-1"
#SELECTOR = "table.product tr td b.priceLarge" 
#REGEX = re.compile("\$(?P<price>[.,\d]+)")

#Best Buy
#URL = "http://www.bestbuy.com/site/Samsung+-+55%22+Class+/+1080p+/+240Hz+/+3D+LED-LCD+HDTV/9798538.p?id=1218176210288&skuId=9798538&st=samsung%20un55c8000&cp=1&lp=1"
#SELECTOR = "div#priceblock div.salenum"
#REGEX = re.compile("\$(?P<price>[.,\d]+)")

#HH Gregg
# URL = "http://www.hhgregg.com/ProductDetail.asp?SID=n&ProductID=37112"
# SELECTOR = "div.displayProductPrice div.ourPrice"
# REGEX = re.compile("Our Price:\$(?P<price>[.,\d]+)")

#Sears
# URL = "http://www.sears.com/shc/s/p_10153_12605_05771160000P?origin=beta&shcapiBypassSSO=true"
# SELECTOR = "div.youPay span.pricing"
# REGEX = re.compile("\$(?P<price>[.,\d]+)")


html = urllib2.urlopen(URL)
parser = etree.HTMLParser(remove_comments=True)
tree = etree.parse(html, parser)

from lxml.cssselect import CSSSelector

sel = CSSSelector(SELECTOR)

price = sel(tree)[0].text.strip('\n\t\r ')
print price
price = REGEX.match(price).group('price').replace(",", "")
print price

#print [e for e in sel(tree)]